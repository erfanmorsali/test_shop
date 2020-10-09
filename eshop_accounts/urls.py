from django.urls import path
from .views import login_page, register_page, log_out, user_profile, edit_profile

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', log_out, name='logout'),
    path('user_profile', user_profile, name='user_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),

]
