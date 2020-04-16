from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from appcatalogs.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


# class ProductAttributeInline(admin.TabularInline):
#     model = ProductAttribute


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'show']
    list_display_links = ['name']
    list_editable = ['show']
    sortable_by = ['created_dt']
    mptt_level_indent = 20


@admin.register(VolumeDesignation)
class VolumeDesignationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'show', 'price_original', 'price_own', 'discount', 'price_discount']
    list_display_links = ['title']
    list_editable = ['show']
    list_filter = ['updated_dt', 'discount', 'brand', 'volume_designation', 'action', 'show']
    search_fields = ['title']
    inlines = (ProductImageInline, )  #ProductAttributeInline)