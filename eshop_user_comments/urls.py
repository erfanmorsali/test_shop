from django.urls import path

from eshop_user_comments.views import contact_us

urlpatterns = [
    path('contact_us', contact_us,name='contact_us'),

]