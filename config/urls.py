from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("apps.core.urls")),
    path("users/", include("apps.users.urls")),
    path("games/", include("apps.games.urls")),
    path("listings/", include("apps.listings.urls")),
    path("orders/", include("apps.orders.urls")),
    path("chat/", include("apps.chat.urls")),
    path("reviews/", include("apps.reviews.urls")),
    path("payments/", include("apps.payments.urls")),
    path("disputes/", include("apps.disputes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)