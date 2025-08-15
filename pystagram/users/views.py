from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    return render(request, "users/login.html", context)
