from django.db import models


class Drone(models.Model):
    brand = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=60)
    context = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_news')

    def __str__(self):
        return self.title
