from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price_purchase','price_selling','quantity','quantity_sold')
    search_fields = ['name']
    list_filter = ('name','price_purchase','price_selling','quantity','quantity_sold')
admin.site.register(Product,ProductAdmin)