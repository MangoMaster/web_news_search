import requests
import bs4
import re

from .models import News

from django.http import HttpResponse

# 人民网爬虫
def spider(request):
    base_url = "http://industry.people.com.cn"
    url = "http://industry.people.com.cn/n1/2018/0913/c413883-30291678.html"
    to_be = ["http://sports.people.com.cn/n1/2018/0913/c14820-30290245.html",
             "http://society.people.com.cn/n1/2018/0913/c1008-30290129.html",
             "http://legal.people.com.cn/n1/2018/0913/c42510-30289770.html",
             "http://industry.people.com.cn/n1/2018/0913/c413883-30291678.html", ]

    # index
    response = requests.get(url)
    # response.encoding = "gb2312"
    # html = response.text
    # soup = bs4.BeautifulSoup(html, features="html.parser")
    # centrals = soup.find_all("ul")
    # for central in centrals:
    #     sub_urls = central.find_all("a")
    #     for sub_url in sub_urls:
    #         to_be.append(base_url + sub_url["href"])

    for i in range(10000000000):
        try:
            # open url
            response = requests.get(to_be[-1])
            base_url = re.match(r'https?://[^/]*', to_be[-1]).group()
            to_be.pop()
            response.encoding = "gb2312"
            html = response.text
            soup = bs4.BeautifulSoup(html, features="html.parser")

            # head
            head = soup.find("head")

            # robots_title
            robots_title = head.find("title").get_text()

            # check duplicate
            if News.objects.filter(robots_title__exact=robots_title):
                continue

            # robots_description
            robots_discription = head.find(
                "meta", {"name": "description"})["content"]

            # published_date
            published_date = head.find(
                "meta", {"name": "publishdate"})["content"]

            # title
            title = soup.find("h1").get_text()

            # passage
            central = soup.find("div", {"id": "rwb_zw"})
            passages = central.find_all("p")
            text = ""
            for passage in passages:
                text += str(passage)

            # sub_url
            # further_reading = soup.find("div", {"id": "rwb_tjyd"})
            # sub_urls = further_reading.find_all("a")
            # for sub_url in sub_urls:
            #     to_be.append(base_url + sub_url["href"])
            about_news = soup.find("div", {"id": "rwb_xgxw"})
            sub_urls = about_news.find_all("a")
            for sub_url in sub_urls:
                to_be.append(sub_url["href"])
            hot_news = soup.find("div", {"id": "rwb_rdtj"})
            sub_urls = hot_news.find_all("a")
            for sub_url in sub_urls:
                to_be.append(base_url + sub_url["href"])
            # brilliant_news = soup.find("div", {"id": "rwb_jctjr"})
            # sub_urls = brilliant_news.find_all("a")
            # for sub_url in sub_urls:
            #     to_be.append(base_url + sub_url["href"])

            # save model
            news = News(robots_title=robots_title, robots_description=robots_discription,
                        title=title, published_date=published_date, text=text, url=response.url)
            news.save()
            print(news)
        except:
            pass
    return HttpResponse("spider working")
