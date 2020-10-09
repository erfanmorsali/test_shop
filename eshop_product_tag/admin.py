from django.contrib import admin
from .models import ProductTag


# Register your models here.


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["__str__", "active"]

    class Meta:
        model = ProductTag


admin.site.register(ProductTag, ProductTagAdmin)
