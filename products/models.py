from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.




class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='دسته بندی')
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'دسته یندی'

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام کالا")
    category = models.ManyToManyField(Category, related_name='product', verbose_name='دسته یندی')
    text = models.TextField(verbose_name='توضحات کالا')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')
    status = models.BooleanField(default=True, verbose_name='موجددی در انبار')
    star = models.IntegerField(null = True, blank = True, default=0)
    image = models.ImageField(upload_to='products/', verbose_name='عکس')
    discount = models.IntegerField(blank = True, null = True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='آدرس دهی')
    test = CKEditor5Field(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        name = ''
        for i in self.title:
            if i == ' ':
                i = '-'
                name += i
            else:
                name += i
        self.slug = name
        super(Product, self).save()

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h4 style="color: red">no image</h4>')

    show_image.short_description = 'تصاویر'

    class Meta:
        verbose_name_plural = 'محصولات'


class Comment(models.Model):
    name = models.CharField(max_length=55, verbose_name='نام', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن')
    created_date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reply_message',
                               verbose_name='پاسخ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "صفحه کامنت محصولات"
        verbose_name_plural = "کامنت های محصولات"