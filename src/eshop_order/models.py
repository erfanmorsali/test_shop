from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده / نشده")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"

    def __str__(self):
        return self.owner.username


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, models.CASCADE, verbose_name="محصول")
    count = models.IntegerField(verbose_name="تعداد")
    price = models.IntegerField(verbose_name="قیمت")
    is_send = models.BooleanField(default=False, verbose_name="ارسال شده / نشده")

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'

    def __str__(self):
        return self.product.title

    def detail_price_sum(self):
        return self.count * self.price
