from django.contrib import admin

# Register your models here.
from eshop_user_comments.models import UserComment


class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'email','is_read']
    list_editable = ['is_read']
    search_fields = ['is_read']


    class Meta:
        model = UserComment


admin.site.register(UserComment,UserCommentAdmin)
