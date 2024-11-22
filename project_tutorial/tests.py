News.objects.all()[:2]
News.objects.oreer_by('pk')
News.objects.all().reverse
News.objects.filter(pk__lte=2)
w=News.objects.get(pk=2)
w.cat
w.cat.name


#qayata aloqa qilish uchun

c=Category.objects.get(pk=2)   # modelga related_name='get_posts'
c.news_set.all()
News.objects.filter(title__contains='li')
News.objects.filter(title__icontains='LI')
News.objects.filter(pk__in=[2,3,4,5], is_published=True)
News.objects.filter(cat__in=[1,2])



connection.queries

from django.db.models import Q
News.objects.filter(Q(pk__lt=1) | Q(cat_id=1))  OR
News.objects.filter(Q(pk__lt=1) & Q(cat_id=1))  AND
News.objects.filter(~Q(pk__lt=1) | Q(cat_id=1))  ne

News.objects.filter(pk__lt=10).count()


News.objects.filter(cat_slug='Jahon')



News.objects.filter(cat__name__contains='on')

Category.objects.filter(news__title__contains='mir')
Category.objects.filter(news__title__contains='mir').distinct()


News.objects.count()
News.objects.aggregate(Min('cat_id'), Max('cat_id'))
News.objects.aggregate(cat_min=Min('cat_id'), cat_max=Max('cat_id'))



News.objects.aggregate(res=Sum('cat_id')- Count('cat_id'))


News.objects.aggregate(res=Avg('cat_id'))


News.objects.values('title', 'cat__name').get(pk=1)
s=News.objects.values('title', 'cat__name')
for p in s:
    print(p['title'], p['cat__name'])




k=Category.objects.annotate(Count('news'))


k[0].news__count

from django.db.models import F
News.objects.filter(pk__gt=F('cat_id'))


from django.db.models.functions import Length

ps=News.objects.annotate(len=Length('title'))
for i in ps:
    print(i.title, i.len)