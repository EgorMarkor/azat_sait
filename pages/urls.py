from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("offerts/", views.offerts, name="offerts"),
    path("oforms/", views.oforms, name="oforms"),
    path("socseti/", views.socseti, name="socseti"),
    path("checkpvz/", views.checkpvz, name="checkpvz"),
    path("checkdanzak/", views.checkdanzak, name="checkdanzak"),
    path("product/<slug:slug>/", views.product, name="product"),
]
