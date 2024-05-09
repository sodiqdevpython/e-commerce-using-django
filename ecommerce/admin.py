from django.contrib import admin
from .models import ProductCategory, Product, Comment, Order

admin.site.register(ProductCategory)
admin.site.register(Comment)
admin.site.register(Order)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)