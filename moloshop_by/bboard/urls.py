# D:\MEGAsync\PycharmProjects\BulletinBoard\moloshop_by\bboard\urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]