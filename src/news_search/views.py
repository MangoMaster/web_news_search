from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
import time
import jieba

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
    search_segs = []

    def get_queryset(self):
        self.search_start_time = time.time()
        # index_object = get_object_or_404(Index, search_text=self.kwargs.get("search_text"))
        search_segs = jieba.cut_for_search(self.kwargs.get("search_text")) 
        index_list = []
        # document search_segs
        self.search_segs = []
        for search_seg in search_segs:
            # prevent blank
            search_seg = search_seg.strip()
            if not search_seg:
                continue
            self.search_segs.append(search_seg)
            
            try:
                index_object = Index.objects.get(
                    search_text=search_seg)
            except:
                continue
                # return News.objects.filter(pk__exact=None)
            index_list += index_object.index.split(',')
        return News.objects.filter(pk__in=index_list).distinct()

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            "search_text": self.kwargs.get("search_text"),
            "search_time": "%.3f" % (time.time() - self.search_start_time),
            "search_segs": self.search_segs,
        })
        return context


class DetailView(generic.DetailView):
    model = News
    template_name = "news_search/detail.html"
