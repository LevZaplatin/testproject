from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    all_articles = Article.objects.all()
    html = ''
    for article in all_articles:
        url = '/news/' + str(article.id) + '/'
        html += '<a href="' + url + '">' + article.title + '<a></br>'
    return HttpResponse(http)

def detail(request, article_id):
    return HttpResponse("<h1>This will be a detailed of article id: " + str(article_id) + "</h1>" )

    
