from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.listings.models import Listing

from .models import Order


@login_required
def create_order_view(request, listing_slug):
    listing = get_object_or_404(
        Listing,
        slug=listing_slug,
        status=Listing.STATUS_ACTIVE
    )

    if listing.seller == request.user:
        messages.error(request, "Нельзя купить своё объявление.")
        return redirect("listings:listing_detail", slug=listing.slug)

    order = Order.objects.create(
        buyer=request.user,
        seller=listing.seller,
        listing=listing,
        price=listing.price,
        quantity=1,
        status=Order.STATUS_PENDING
    )

    messages.success(request, "Заказ создан.")
    return redirect("orders:order_detail", order_id=order.id)


@login_required
def order_list_view(request):
    orders = Order.objects.filter(buyer=request.user)

    context = {
        "orders": orders,
    }

    return render(request, "orders/order_list.html", context)


@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.buyer != request.user and order.seller != request.user:
        messages.error(request, "У вас нет доступа к этому заказу.")
        return redirect("core:home")

    context = {
        "order": order,
    }

    return render(request, "orders/order_detail.html", context)


@login_required
def my_sales_view(request):
    sales = Order.objects.filter(seller=request.user)

    context = {
        "sales": sales,
    }

    return render(request, "orders/my_sales.html", context)


@login_required
def complete_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user)

    if order.status not in [Order.STATUS_CANCELLED, Order.STATUS_COMPLETED]:
        order.status = Order.STATUS_COMPLETED
        order.save()

        messages.success(request, "Заказ завершён.")

    return redirect("orders:order_detail", order_id=order.id)


@login_required
def cancel_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user)

    if order.status not in [Order.STATUS_COMPLETED, Order.STATUS_CANCELLED]:
        order.status = Order.STATUS_CANCELLED
        order.save()

        messages.success(request, "Заказ отменён.")

    return redirect("orders:order_detail", order_id=order.id)