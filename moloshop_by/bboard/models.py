# D:\MEGAsync\PycharmProjects\BulletinBoard\moloshop_by\bboard\models.py

from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Toвap')  # заголовок объявления с названием продаваемого товара (тип — строковый, длина — 50 символов). Поле, обязательное к заполнению;
    content = models.TextField(null=True, blank=True, verbose_name='Oпиcaниe')  # сам текст объявления, описание товара (тип — memo);
    price = models.FloatField(null=True, blank=True, verbose_name='Цeнa')  # цена (тип — вещественное число);
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')  # дата публикации (тип — временнáя отметка, значение по умолчанию — текущие дата и время, индексированное).
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name= 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Haзвaниe')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']