from django.contrib.auth.models import User
from django.db import models

from apps.listings.models import Listing


class Order(models.Model):
    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    STATUS_DISPUTE = "dispute"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Ожидает оплаты"),
        (STATUS_PAID, "Оплачен"),
        (STATUS_IN_PROGRESS, "В процессе"),
        (STATUS_COMPLETED, "Завершён"),
        (STATUS_CANCELLED, "Отменён"),
        (STATUS_DISPUTE, "Спор"),
    ]

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sales"
    )
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.id} — {self.listing.title}"

    @property
    def total_price(self):
        return self.price * self.quantity