from django.shortcuts import render, redirect
from .models import Feed, User

def home(request):
    rooms = Feed.objects.all()
    context= {'rooms':rooms}
    return render(request, 'base/home.html', context)

def feed(request,pk):
    rooms= Feed.objects.get(id=pk)
    context= {"rooms":rooms}
    return render(request, 'base/feed.html', context)