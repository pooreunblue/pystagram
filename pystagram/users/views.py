from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print("form.is_valid():", form.is_valid())
        print("form.cleaned_data:", form.cleaned_data)
        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)
