from django.shortcuts import render, redirect

def feeds(request):
    return render(request, "posts/feeds.html")
