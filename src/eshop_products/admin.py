from django.contrib import admin
from .models import Product,FavouriteProducts,ProductGallery


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'active']
    list_editable = ['active']
    search_fields = ['title']


admin.site.register(Product, ProductAdmin)
admin.site.register(FavouriteProducts)
admin.site.register(ProductGallery)
