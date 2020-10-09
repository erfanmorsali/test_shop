import itertools

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from eshop_order.forms import OrderDetailForm
from eshop_product_category.models import ProductCategory
from .models import Product, FavouriteProducts, ProductGallery
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from eshop_product_tag.models import ProductTag


# Create your views here.


class ProductList(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.get_active_product()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, slug, product_id):
    message = messages.get_messages(request)
    product = Product.objects.filter(active=True, slug=slug, id=product_id).first()
    if product is None :
        raise Http404("محصولی با این مشخصات یافت نشد")

    product.visit += 1
    product.save()
    tags = ProductTag.objects.filter(product=product)
    product_gallery = ProductGallery.objects.filter(product=product)
    grouped_product_gallery = list(my_grouper(3, product_gallery))
    related_product = Product.objects.filter(category__product=product).distinct()
    grouped_related_products = list(my_grouper(3, related_product))
    order_detail_form = OrderDetailForm(request.POST or None, initial={"productId": product.id})
    context = {
        "related_products": grouped_related_products,
        "tags": tags,
        'product': product,
        'order_detail_form': order_detail_form,
        "message": message,
        "product_gallery": grouped_product_gallery
    }
    return render(request, 'products/product_detail.html', context)


def category_render_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'category_render_partial.html', context)


class ProductByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name=category_name).first()
        return Product.objects.filter(category=category)


class ProductByTag(ListView):
    template_name = "products/product_list.html"
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        tag_slug = self.kwargs['product_tag']
        print(tag_slug)
        tag = ProductTag.objects.filter(slug=tag_slug).first()
        return Product.objects.filter(tag=tag)


@login_required(login_url='/login')
def add_favourite_product(request, product_id):
    product = Product.objects.filter(id=product_id, active=True).first()
    FavouriteProducts.objects.create(user_id=request.user.id, product=product)

    messages.success(request, "محصول با موفقت به محصولات مورد علاقه اضافه شد")
    return redirect("/")


class UserFavouriteProducts(ListView):
    template_name = "products/favourite_products.html"
    paginate_by = 2

    def get_queryset(self):
        request = self.request
        user_id = request.user.id
        product = FavouriteProducts.objects.filter(user_id=user_id)
        if product is None:
            return product
        return Product.objects.filter(favouriteproducts__user_id=user_id, active=True).distinct()


class SearchProduct(ListView):
    template_name = "products/product_list.html"
    paginate_by = 2

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is None:
            return Product.objects.all()
        return Product.objects.search_product(query)
