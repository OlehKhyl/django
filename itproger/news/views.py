from django.shortcuts import render
from .models import Articles

# Create your views here.

def news_home(requst):
    news = Articles.objects.all()
    return render(requst, 'news/news_home.html', {'news' : news})