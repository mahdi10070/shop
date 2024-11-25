# Generated by Django 5.1.1 on 2024-11-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'صفحه کامنت محصولات', 'verbose_name_plural': 'کامنت های محصولات'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='ایمیل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=55, verbose_name='نام'),
            preserve_default=False,
        ),
    ]
