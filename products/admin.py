from django.contrib import admin
from .models import Color, Product, Category, SubCategory, Market, ProductImage
from .translation import CustomTranslationsAdmin


class ImgAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(CustomTranslationsAdmin):
    list_display = ['name']
    inlines = [SubCategoryInline]


@admin.register(Product)
class ProductAdmin(CustomTranslationsAdmin):
    inlines = [ImgAdmin]
    filter_horizontal = ['colors']


admin.site.register(Color)
admin.site.register(Market)
