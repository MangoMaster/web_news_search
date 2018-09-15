import jieba

from .models import News, Index

from django.http import HttpResponse


def invert(request):
    # filter
    newss = News.objects.filter(pk__gt=8395)

    # seg words
    for news in newss:
        seg_set = set(jieba.cut_for_search(news.text))
        seg_set |= set((jieba.cut_for_search(news.robots_title)))
        # invert index
        for seg in seg_set:
            try:
                index = Index.objects.get(search_text__exact=seg)
            except Index.DoesNotExist:  # not exist
                index = Index(search_text=seg, index=str(news.pk), count=1)
                index.save()
            except:
                pass
            else:  # exist
                index.count += 1
                index.index += "," + str(news.pk)
                index.save()

    return HttpResponse("inverting index")
