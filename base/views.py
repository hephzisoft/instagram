from django.shortcuts import render, redirect, reverse
from .models import Feed, User, Like
from django.http import HttpResponseRedirect


def home(request):
    rooms = Feed.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def feed(request, pk):
    rooms = Feed.objects.get(id=pk)
    context = {"rooms": rooms}
    return render(request, 'base/feed.html', context)


def like(request, pk):
    user = request.user
    post = Feed.objects.get(id=pk)
    current_likes = post.likes
    liked = Like.objects.filter(user=user, post=post).count()
    if not liked:
        liked = Like.objects.create(user=user, post=post)
        current_likes += 1
    else:
        liked = Like.objects.create(user=user, post=post).delete()
        current_likes -= 1
    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('feed', args=[pk]))
