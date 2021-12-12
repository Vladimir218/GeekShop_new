from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import re_path
from django.urls.conf import path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
    path("", include("social_django.urls", namespace="social")),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
