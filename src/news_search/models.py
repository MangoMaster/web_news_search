from django.db import models

# Create your models here.


class News(models.Model):
    robots_title = models.CharField(max_length=100)
    robots_description = models.TextField()
    title = models.CharField(max_length=50)
    published_date = models.DateField()
    text = models.TextField()
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.robots_title


class Index(models.Model):
    word = models.CharField(max_length=10)
    index = models.TextField()
    size = models.IntegerField()

    def __str__(self):
        return self.word
