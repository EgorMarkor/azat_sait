from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin-panel/", views.admin_panel, name="admin_panel"),
    path("catalog/", views.catalog, name="catalog"),
    path("offerts/", views.offerts, name="offerts"),
    path("oforms/", views.oforms, name="oforms"),
    path("socseti/", views.socseti, name="socseti"),
    path("checkpvz/", views.checkpvz, name="checkpvz"),
    path("checkdanzak/", views.checkdanzak, name="checkdanzak"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("public-offer/", views.public_offer, name="public_offer"),
    path("personal-data/", views.personal_data, name="personal_data"),
    path("user-agreement/", views.user_agreement, name="user_agreement"),
    path("contacts/", views.contacts, name="contacts"),
    path("product/<slug:slug>/", views.product, name="product"),
]
