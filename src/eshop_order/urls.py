from django.urls import path
from .views import add_user_order, user_order_items,delete_order_item

urlpatterns = [
    path('add-user-order', add_user_order, name='add-user-order'),
    path('delete_order_item/<item_id>', delete_order_item, name='delete_order_item'),
    path('user_order_items', user_order_items, name='user_order_items')
]
