# Generated by Django 5.1.1 on 2024-11-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='آدرس'),
        ),
    ]