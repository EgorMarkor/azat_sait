from django.shortcuts import render


def home(request):
    return render(request, "pages/index.html")


def catalog(request):
    return render(request, "pages/catalog.html")


def offerts(request):
    return render(request, "pages/offerts.html")


def oforms(request):
    return render(request, "pages/oforms.html")


def socseti(request):
    return render(request, "pages/socseti.html")


def checkpvz(request):
    return render(request, "pages/checkpvz.html")


def checkdanzak(request):
    return render(request, "pages/checkdanzak.html")


def product(request, slug):
    products = {
        "stroy-canvas-jacket": {
            "id": "stroy-canvas-jacket",
            "title": "STROY Canvas Jacket",
            "price": 6500,
            "description": [
                "100% хлопок",
                "Прямой крой",
                "Усиленные швы",
                "Лого STROY на груди",
                "Графика на спине",
                "Глубокий черный",
            ],
            "fit": [
                "Свободная посадка",
                "Длина до бедра",
                "Размер на модели: M",
            ],
        },
        "hoodie-logo-chained": {
            "id": "hoodie-logo-chained",
            "title": "Hoodie Logo Chained",
            "price": 6500,
            "description": [
                "100% хлопок",
                "Классический крой",
                "Капюшон с утяжкой",
                "Лого CHAINED на груди",
                "Графика на спине",
                "Черный цвет",
            ],
            "fit": [
                "Свободная посадка",
                "Размер на модели: M",
                "Рост модели: 182 см",
            ],
        },
    }
    if slug.startswith("hoodie-chained"):
        product = {
            "id": slug,
            "title": "Hoodie Chained Black",
            "price": 6500,
            "description": [
                "100% хлопок",
                "Классический крой",
                "Капюшон с утяжкой",
                "Лого NGG на груди",
                "Графика 04 на спине",
                "Серый меланж",
            ],
            "fit": [
                "Оверсайз посадка",
                "Размер на модели: L",
                "Рост модели: 184 см",
            ],
        }
    else:
        product = products.get(slug, products["hoodie-logo-chained"])
        product["id"] = slug
    return render(request, "pages/product.html", {"product": product})


def admin_panel(request):
    return render(request, "pages/admin.html")


def privacy_policy(request):
    return render(request, "pages/privacy.html")


def public_offer(request):
    return render(request, "pages/public_offer.html")


def personal_data(request):
    return render(request, "pages/personal_data.html")


def user_agreement(request):
    return render(request, "pages/user_agreement.html")


def contacts(request):
    return render(request, "pages/contacts.html")
