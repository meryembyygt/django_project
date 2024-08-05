from django.shortcuts import render

# Create your views here.

def list(request):
        return render(request, 'news/list.html')

def detail(request, news_id:int):
        return render(request, 'news/detail.html', {"nid":news_id})
