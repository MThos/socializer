import datetime

from django.shortcuts import render, redirect
from django.urls import resolve
from django.utils import translation

from .forms import SignupForm
from .models import User


def index(request):
    year = datetime.datetime.now().year
    title = resolve(request.path).app_name.capitalize()
    get_current_language = translation.get_language()
    return render(request, "registration/index.html", {
        "year": year,
        "title": "Sign up",
        "tab_title": "Sign up - Socializer",
        "sub_title": "SOCIALIZER",
        "get_current_language": get_current_language
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'],
            full_name = form.cleaned_data['full_name'],
            user_name = form.cleaned_data['user_name'],
            password = form.cleaned_data['password']
            user = User(email=email, full_name=full_name, user_name=user_name, password=password, signup=datetime.datetime.now(), logins=0, last_login=datetime.datetime.now())
            user.save()
            signed_up = "Congratulations! You are now signed up, " + full_name[0] + "."
        else:
            print(form.errors)
            return redirect("/registration/")

    return render(request, "registration/signup.html", {
        "signed_up": signed_up,
        "full_name": full_name
    })