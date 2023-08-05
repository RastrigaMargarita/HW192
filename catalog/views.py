from django.shortcuts import render
from catalog.models import UserContact, Product


def index(request):
    """Отображаем первую страницу, выводим первые три продукта в карточки, если база данных не пуста"""

    try:
        item_count = 0
        products_list_3 = {}
        for item in Product.objects.all():
            item_count += 1
            products_list_3[f"title{item_count}"] = item.title
            products_list_3[f"price{item_count}"] = item.price
            products_list_3[f"description{item_count}"] = item.description
            if item_count > 3:
                break
        return render(request, "catalog/index.html", context=products_list_3)
    except Exception:
        return render(request, "catalog/index.html")


def contacts_post(request):
    """Передаем в базу данных то что прислал пользователь"""

    if request.method == 'POST':
        UserContact.objects.create(name=request.POST.get('name'),
                                   phone=request.POST.get('phone'),
                                   message=request.POST.get('message'))

    return render(request, 'catalog/contacts.html')
