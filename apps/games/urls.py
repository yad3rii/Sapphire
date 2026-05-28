from django.urls import path

from . import views


app_name = "games"

urlpatterns = [
    path("", views.game_list_view, name="game_list"),
    path("<slug:slug>/", views.game_detail_view, name="game_detail"),
]