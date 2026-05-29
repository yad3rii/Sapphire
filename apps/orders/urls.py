from django.urls import path

from . import views


app_name = "orders"

urlpatterns = [
    path("", views.order_list_view, name="order_list"),
    path("sales/", views.my_sales_view, name="my_sales"),
    path("create/<slug:listing_slug>/", views.create_order_view, name="create_order"),
    path("<int:order_id>/", views.order_detail_view, name="order_detail"),
    path("<int:order_id>/complete/", views.complete_order_view, name="complete_order"),
    path("<int:order_id>/cancel/", views.cancel_order_view, name="cancel_order"),
]