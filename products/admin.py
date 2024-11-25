from django.contrib import admin
from . import models



# Register your models here.

class CommentInView(admin.StackedInline):
    model = models.Comment


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'show_image')
    list_filter = ('category', 'title')
    search_fields = ('title',)
    inlines = (CommentInView,)



admin.site.register(models.Category)
admin.site.register(models.Comment)
