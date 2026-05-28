from django.urls import path

from . import views


app_name = "listings"

urlpatterns = [
    path("", views.listing_list_view, name="listing_list"),
    path("create/", views.listing_create_view, name="listing_create"),
    path("my/", views.my_listings_view, name="my_listings"),
    path("<slug:slug>/", views.listing_detail_view, name="listing_detail"),
    path("<slug:slug>/edit/", views.listing_update_view, name="listing_update"),
]