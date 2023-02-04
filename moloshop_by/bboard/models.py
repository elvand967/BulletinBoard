from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)  # заголовок объявления с названием продаваемого товара (тип — строковый, длина — 50 символов). Поле, обязательное к заполнению;
    content = models.TextField(null=True, blank=True)  # сам текст объявления, описание товара (тип — memo);
    price = models.FloatField(null=True, blank=True)  # цена (тип — вещественное число);
    published = models.DateTimeField(auto_now_add=True, db_index=True)  # дата публикации (тип — временнáя отметка, значение по умолчанию — текущие дата и время, индексированное).
