from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                auth_login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                if User.objects.filter(username=username).exists():
                    raise IntegrityError("This username is already taken")
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                    )
                    auth_login(request, user)
                    return redirect("list_projects")
            else:
                form.add_error("password", "the passwords do not match")
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
