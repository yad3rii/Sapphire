from django.contrib.auth.models import User
from django.db import models

from apps.games.models import Category, Game


class Listing(models.Model):
    STATUS_ACTIVE = "active"
    STATUS_HIDDEN = "hidden"
    STATUS_SOLD = "sold"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Активно"),
        (STATUS_HIDDEN, "Скрыто"),
        (STATUS_SOLD, "Продано"),
    ]

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="listings"
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="listings"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="listings",
        blank=True,
        null=True
    )
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(
        upload_to="listings/",
        blank=True,
        null=True
    )
    delivery_info = models.TextField(
        blank=True,
        help_text="Как продавец передаст товар покупателю"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title