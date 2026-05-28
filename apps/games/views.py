from django.shortcuts import get_object_or_404, render

from .models import Game


def game_list_view(request):
    games = Game.objects.all()

    context = {
        "games": games,
    }

    return render(request, "games/game_list.html", context)


def game_detail_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    categories = game.categories.all()

    context = {
        "game": game,
        "categories": categories,
    }

    return render(request, "games/game_detail.html", context)