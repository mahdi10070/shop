from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator
# Create your models here.

class CategoryBlog(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', verbose_name='نویسنده')
    main_keyboard = models.CharField(max_length=100, verbose_name='کلمه کلیدی')
    text = CKEditor5Field(verbose_name="متن")
    featured_image = models.ImageField(upload_to='featured_images', verbose_name='تصویر شاخص')
    seo_title = models.CharField(max_length=100, verbose_name='عنوان سئو')
    meta_description = models.TextField(verbose_name='توضیحات متا')
    create_at = models.DateTimeField(auto_now_add=True)
    create_updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(CategoryBlog, related_name='blog', verbose_name='دسته یندی')
    slug = models.SlugField(max_length=100 ,blank=True, null=True, verbose_name='آدرس')

    def __str__(self):
        return self.main_keyboard

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.slug is None:
            translator = Translator()
            translation = translator.translate(self.main_keyboard, src='fa', dest='en')
            self.slug = slugify(translation.text)
            super(Blog, self).save()
        else:
            super(Blog, self).save()

    class Meta:
        verbose_name_plural = 'مقالات'

