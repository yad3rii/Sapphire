from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "game",
            "category",
            "title",
            "slug",
            "description",
            "price",
            "quantity",
            "image",
            "delivery_info",
            "status",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "delivery_info": forms.Textarea(attrs={"rows": 4}),
        }