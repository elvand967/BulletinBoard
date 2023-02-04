# D:\MEGAsync\PycharmProjects\BulletinBoard\moloshop_by\moloshop_by\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
]