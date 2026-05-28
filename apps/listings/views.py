from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListingForm
from .models import Listing


def listing_list_view(request):
    listings = Listing.objects.filter(status=Listing.STATUS_ACTIVE)

    query = request.GET.get("q")
    game = request.GET.get("game")
    category = request.GET.get("category")

    if query:
        listings = listings.filter(title__icontains=query)

    if game:
        listings = listings.filter(game__slug=game)

    if category:
        listings = listings.filter(category__slug=category)

    context = {
        "listings": listings,
        "query": query,
    }

    return render(request, "listings/listing_list.html", context)


def listing_detail_view(request, slug):
    listing = get_object_or_404(Listing, slug=slug)

    context = {
        "listing": listing,
    }

    return render(request, "listings/listing_detail.html", context)


@login_required
def listing_create_view(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()

            messages.success(request, "Объявление создано.")
            return redirect("listings:listing_detail", slug=listing.slug)
    else:
        form = ListingForm()

    return render(request, "listings/listing_create.html", {"form": form})


@login_required
def listing_update_view(request, slug):
    listing = get_object_or_404(Listing, slug=slug, seller=request.user)

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=listing)

        if form.is_valid():
            form.save()
            messages.success(request, "Объявление обновлено.")
            return redirect("listings:listing_detail", slug=listing.slug)
    else:
        form = ListingForm(instance=listing)

    context = {
        "form": form,
        "listing": listing,
    }

    return render(request, "listings/listing_update.html", context)


@login_required
def my_listings_view(request):
    listings = Listing.objects.filter(seller=request.user)

    context = {
        "listings": listings,
    }

    return render(request, "listings/my_listings.html", context)