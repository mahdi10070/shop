# Generated by Django 5.1.1 on 2024-11-18 10:34

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
