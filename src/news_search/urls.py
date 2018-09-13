from django.urls import path

from . import views
from . import spider

app_name = "news_search"
urlpatterns = [
    path('', views.search_main, name="search_main"),
    path('?search_text=<str:search_text>/', views.search, name='search'),
    path('results/', views.search_results, name="results"),
    path('spider/', spider.spider),
]
