from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This will be a list of news articles</h1>")

def detail(request, article_id):
    return HttpResponse("<h1>This will be a detailed of article id: " + str(article_id) + "</h1>" )

    
