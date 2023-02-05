
# D:\MEGAsync\PycharmProjects\BulletinBoard\moloshop_by\bboard\admin.py

from django.contrib import admin
from .models import Bb
from .models import Rubric


class BbAdmin (admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
