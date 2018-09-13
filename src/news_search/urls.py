from django.urls import path

from . import views
from . import spider
from . import invert

app_name = "news_search"
urlpatterns = [
    path('', views.SearchMainView.as_view(), name="search_main"),
    path('search/', views.search, name='search'),
    path('results/<str:search_text>/<int:page>/',
         views.SearchResultsView.as_view(), name="search_results"),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('spider/', spider.spider),
    path('invert/', invert.invert),
]
