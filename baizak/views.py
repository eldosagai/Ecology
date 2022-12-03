from django.shortcuts import render, redirect
from .models import Article, ArticleImage, Event, EventImage
# import pandas as pd
# Create your views here.

def ViewArticles(request,id):
    article = Article.objects.get(id=id)
    print(article)
    images = ArticleImage.objects.all()
    # print(pd.DataFrame(Article.objects.all().values())) 
    return render(request,'news.html',{'article':article, 'images':images})
        
def ViewEvents(request,id):
    events = Event.objects.get(id=id)
    images = EventImage.objects.all()
    return render(request,'event.html',{'events': events, 'images': images})

def Eco(request):
    return render(request,'eco.html')

def MainPage(request):
    articles = Article.objects.all()
    events = Event.objects.all()
    return render(request,'index.html',{'articles':articles,'events':events})