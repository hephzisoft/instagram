from django.shortcuts import render, redirect, reverse
from .models import Feed, User, Like
from django.http import HttpResponseRedirect
from django

@login_required()
def home(request):
    posts = Feed.objects.all()
    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def feed(request, post_id):
    post = Feed.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'base/feed.html', context)


def like(request, post_id):
    user = request.user
    post = Feed.objects.get(id=post_id)
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
    return HttpResponseRedirect(reverse('feed', args=[post_id]))


def login(request):
    