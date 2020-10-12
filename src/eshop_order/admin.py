from django.contrib import admin
from .models import OrderDetails, Order


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "is_paid"]
    list_editable = ["is_paid"]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["__str__", "is_send","price" , "count"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails,OrderDetailAdmin)
