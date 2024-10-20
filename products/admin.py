from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'show_image')
    list_filter = ('category', 'title')
    search_fields = ('title', )

admin.site.register(models.Category)


