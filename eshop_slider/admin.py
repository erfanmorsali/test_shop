from django.contrib import admin
from .models import Slider


# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'thumbnail_slider_image', 'link']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
