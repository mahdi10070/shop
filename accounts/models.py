from django.contrib.auth.models import User
from django.db import models

from products.models import Product, Category



# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet', verbose_name='کاربر')
    product = models.ManyToManyField(Product, related_name='wallet', verbose_name='محصول', null=True, blank=True)
    count = models.IntegerField(default=0)
    money = models.IntegerField(default=0, verbose_name='پول')

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name_plural = 'کیف پول'


class Address(models.Model):
    user = models.ForeignKey(User, related_name='address', on_delete=models.CASCADE, verbose_name='کاربر')
    address = models.TextField()
    phone = models.CharField(max_length=22)
    postal_code = models.CharField(max_length=22)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'آدرس'

class Information(models.Model):
    user = models.ForeignKey(User, related_name='information', on_delete=models.CASCADE, verbose_name='کاربر')
    like_product = models.ManyToManyField(Product, related_name='information', null = True, blank = True, verbose_name='علاقمند')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='information', blank=True, null=True, verbose_name='آدرس')


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'مشخصات کاربران'



