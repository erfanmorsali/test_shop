from django.db import models


# Create your models here.


class ProductTag(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="عنوان در url")
    active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
