from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from appcatalogs.models import ProductImage, ProductAttribute, Product, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'sort']
    list_editable = ['sort']
    sortable_by = ['sort']
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'show']
    list_display_links = ['title']
    inlines = (ProductImageInline, ProductAttributeInline)