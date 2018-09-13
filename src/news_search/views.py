from django.shortcuts import render

# Create your views here.

def search_main(request):
    return render(request, "news_search/search.html")

def search(request):
    pass

def search_results(request, word):
    pass