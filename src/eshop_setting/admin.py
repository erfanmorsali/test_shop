from django.contrib import admin

# Register your models here.
from eshop_setting.models import SiteSetting


class SiteSettingAddmin(admin.ModelAdmin):
    list_display = ['__str__', 'address','email', 'phone']

    class Meta:
        model = SiteSetting


admin.site.register(SiteSetting, SiteSettingAddmin)
