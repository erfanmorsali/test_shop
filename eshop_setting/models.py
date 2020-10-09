from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ی ما')
    logo = models.ImageField(upload_to='logo/', verbose_name='لوگو')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اطلاعات ما'
        verbose_name_plural = 'اطلاعات ما'
