from django.shortcuts import render
from .forms import OrderDetailForm
from .models import Order, OrderDetails
from eshop_products.models import Product
from django.contrib import messages
from django.shortcuts import redirect, Http404
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login")
def add_user_order(request):
    form = OrderDetailForm(request.POST or None)
    if form.is_valid():
        user_id = request.user.id
        order = Order.objects.filter(owner_id=user_id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=user_id, is_paid=False)
        product_id = form.cleaned_data.get("productId")
        count = form.cleaned_data.get("count")
        if count < 0:
            count = 1
        product = Product.objects.filter(id=product_id, active=True).first()
        print(product)
        if product is None:
            raise Http404("محصولی با این مشخصات یافت نشد")
        OrderDetails.objects.create(order=order, product_id=product.id, count=count, price=product.price, is_send=False)
        messages.success(request, "محصول با موفقت به سبد خرید اضافه شد")
        return redirect(f"/products/{product.slug}/{product.id}")


@login_required(login_url="/login")
def delete_order_item(request, item_id):
    OrderDetails.objects.filter(id=item_id, order__owner_id=request.user.id).delete()
    return redirect("/user_order_items")


@login_required(login_url="/login")
def user_order_items(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is None:
        raise Http404("کاربر هیچ محصولی در سبد خرید خود ندارد")
    else:
        order_items = OrderDetails.objects.filter(order=order)
    context = {
        "order": order_items
    }
    return render(request, "order.html", context)
