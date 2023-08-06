from django.shortcuts import render
from catalog.models import UserContact, Product


def index(request):
    """Отображаем первую страницу, выводим первые три продукта в карточки, если база данных не пуста"""

    try:
        return render(request, "catalog/index.html", context={"object_list": Product.objects.all()})
    except Exception:
        return render(request, "catalog/index.html")


def contacts_post(request):
    """Передаем в базу данных то что прислал пользователь"""

    if request.method == 'POST':
        UserContact.objects.create(name=request.POST.get('name'),
                                   phone=request.POST.get('phone'),
                                   message=request.POST.get('message'))

    return render(request, 'catalog/contacts.html')

def item(request, item_id):
    """Показывам карточку товара"""

    return render(request, 'catalog/item.html', {'item': Product.objects.get(id=item_id)})