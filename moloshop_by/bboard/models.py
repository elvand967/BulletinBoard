# D:\MEGAsync\PycharmProjects\BulletinBoard\moloshop_by\bboard\models.py

from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Toвap')  # заголовок объявления с названием продаваемого товара (тип — строковый, длина — 50 символов). Поле, обязательное к заполнению;
    content = models.TextField(null=True, blank=True, verbose_name='Oпиcaниe')  # сам текст объявления, описание товара (тип — memo);
    price = models.FloatField(null=True, blank=True, verbose_name='Цeнa')  # цена (тип — вещественное число);
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')  # дата публикации (тип — временнáя отметка, значение по умолчанию — текущие дата и время, индексированное).

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name= 'Объявление'
        ordering = ['-published']