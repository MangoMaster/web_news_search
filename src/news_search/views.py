from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
import time

# Create your views here.
from .models import News, Index


class SearchMainView(generic.TemplateView):
    template_name = "news_search/search_main.html"


def search(request):
    text = request.GET["search_text"]
    if text:
        return HttpResponseRedirect(reverse('news_search:search_results', args=(text, 1)))
    else: # no text in request
        return HttpResponseRedirect(reverse('news_search:search_main'))


class SearchResultsView(generic.ListView):
    model = News
    paginate_by = 10
    template_name = "news_search/search_results.html"
    search_start_time = time.time()

    def get_queryset(self):
        self.search_start_time = time.time()
        # index_object = get_object_or_404(Index, search_text=self.kwargs.get("search_text"))
        search_text = self.kwargs.get("search_text")#.split(' ')
        try:
            index_object = Index.objects.get(
                search_text=search_text)
        except:
            return News.objects.filter(pk__exact=None)
        index_list = index_object.index.split(',')
        return News.objects.filter(pk__in=index_list)

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            "search_text": self.kwargs.get("search_text"),
            "search_time": "%.3f" % (time.time() - self.search_start_time),
        })
        return context


class DetailView(generic.DetailView):
    model = News
    template_name = "news_search/detail.html"
