from django.urls import path
from .views import ProductList, ProductByCategory, category_render_partial, product_detail, add_favourite_product, \
    UserFavouriteProducts, SearchProduct, ProductByTag

urlpatterns = [
    path('product_list', ProductList.as_view(), name='product_list'),
    path('prodcut_categories_partial', category_render_partial, name='category_render_partial'),
    path('products/<category_name>', ProductByCategory.as_view(), name='ProductByCategory'),
    path('product_tags/<product_tag>', ProductByTag.as_view(), name='ProductByTag'),
    path('products/<slug>/<product_id>', product_detail, name='product_detail'),
    path('add_favourite_product/<product_id>', add_favourite_product, name='add_favourite_product'),
    path('user_f_products', UserFavouriteProducts.as_view(), name='user_favourite_products'),
    path('product/search', SearchProduct.as_view()),
]
