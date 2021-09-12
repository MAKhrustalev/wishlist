from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """ Таблица "Товар"

    id
    Название товара
    Ссылка на товар
    Цена товара
    Дата и время создания записи
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """ Таблица "Лист подарков"

    id
    Название листа
    Владелец листа
    Продукт - ManyToMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
