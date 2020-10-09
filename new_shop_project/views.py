from django.shortcuts import render
from eshop_setting.models import SiteSetting
from eshop_slider.models import Slider
from django.contrib import messages
from eshop_products.models import Product
import itertools
from eshop_product_category.models import ProductCategory


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    message = messages.get_messages(request)
    most_visited_products = Product.objects.order_by("-visit").all()[:8]
    grouped_most_visited_products = list(my_grouper(4, most_visited_products))
    latest_products = Product.objects.order_by("-id").all()[:8]
    grouped_latest_products = list(my_grouper(4, latest_products))
    product_groups = ProductCategory.objects.all()

    sliders = Slider.objects.all()

    context = {
        'message': message,
        'sliders': sliders,
        "most_visited_products": grouped_most_visited_products,
        "latest_products": grouped_latest_products,
        "product_groups": product_groups,
    }
    return render(request, 'home_page.html', context)


def about_us(request):
    site_information = SiteSetting.objects.last()
    context = {
        'information': site_information
    }
    return render(request, 'about_us.html', context)


def footer(request, *args, **kwargs):
    information = SiteSetting.objects.last()
    context = {
        'information': information
    }
    return render(request, 'shared/Footer.html', context)
