# Generated by Django 5.1.1 on 2024-11-12 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestBlog',
        ),
    ]
