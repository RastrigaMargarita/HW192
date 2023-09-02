from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="наименование", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание")
    picture = models.ImageField(verbose_name="изображение (превью)")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="цена за покупку")
    creation_date = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    last_changing_date = models.DateTimeField(verbose_name="дата последнего изменения", auto_now_add=True)
    slug = models.SlugField(max_length=255, verbose_name="slug", db_index=True, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="наименование", unique=True)
    description = models.CharField(max_length=500, verbose_name="описание")

    def __str__(self):
        return self.title


class Usercontact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.message}"


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Компания", unique=True)


class Version(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    nomer = models.IntegerField(verbose_name="Номер версии")
    version_title = models.CharField(verbose_name="Название версии")
    current_version = models.BooleanField(verbose_name="Текущая версия", default=True)

    def __str__(self):
        return self.version_title
