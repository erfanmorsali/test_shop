from django.db import models
from django.utils.html import format_html


# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="sliders/", null=True, verbose_name="تصویر")
    link = models.URLField(verbose_name="لینک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def thumbnail_slider_image(self):
        return format_html(f"<img style='border-radius: 30px;' src={self.image.url} width=150px height=150px alt={self.title} >")

    thumbnail_slider_image.short_description = "تصویر اسلایدر"
