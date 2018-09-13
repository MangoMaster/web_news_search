import jieba

from .models import News, Index

from django.http import HttpResponse


def invert(request):
    # clear index
    Index.objects.all().delete()

    # seg words
    for news in News.objects.all():
        seg_set = set(jieba.cut_for_search(news.text))
        seg_set |= set((jieba.cut_for_search(news.robots_title)))
        # invert index
        for seg in seg_set:
            try:
                index = Index.objects.get(word__exact=seg)
            except Index.DoesNotExist:  # not exist
                index = Index(word=seg, index=str(news.pk), size=1)
                index.save()
            except:
                pass
            else:  # exist
                index.size += 1
                index.index += "," + str(news.pk)
                index.save()

    return HttpResponse("inverting index")
