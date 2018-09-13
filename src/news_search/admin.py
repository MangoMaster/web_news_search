from django.contrib import admin

# Register your models here.
from .models import News, Index

admin.site.register(News)
admin.site.register(Index)
