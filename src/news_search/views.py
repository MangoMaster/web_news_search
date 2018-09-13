from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import News, Index


class SearchMainView(generic.TemplateView):
    template_name = "news_search/search_main.html"


def search(request):
    text = request.GET["search_text"]
    return HttpResponseRedirect(reverse('news_search:search_results', args=(text, 1)))


class SearchResultsView(generic.ListView):
    model = News
    paginate_by = 10
    template_name = "news_search/search_results.html"

    def get_queryset(self):
        index_object = get_object_or_404(Index, search_text=self.kwargs.get("search_text"))
        index_list = index_object.index.split(',')
        return News.objects.filter(pk__in=index_list)


class DetailView(generic.DetailView):
    model = News
    template_name = "news_search/detail.html"
