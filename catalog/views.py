from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "catalog/index.html")


def contacts_post(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        with open("user_returns.txt", mode="a") as file:
            file.write(f"{name}, {phone}, {message}")

    return render(request, 'catalog/contacts.html')
