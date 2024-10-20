from django.db import models
from django.utils.html import format_html


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
    image = models.ImageField(upload_to='products/', verbose_name='عکس')
    discount = models.IntegerField(blank = True, null = True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='آدرس دهی')

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


