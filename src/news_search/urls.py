from django.urls import path

from . import views
from . import spider
from . import invert

app_name = "news_search"
urlpatterns = [
    path('', views.search_main, name="search_main"),
    path('search/', views.search, name='search'),
    path('results/<str:search_text>', views.search_results, name="search_results"),

    path('spider/', spider.spider),
    path('invert/', invert.invert),
]
