import datetime

from django.shortcuts import render
from django.urls import resolve
from django.utils import translation

from .models import User
from .forms import SignupForm


def index(request):
    year = datetime.datetime.now().year
    title = resolve(request.path).app_name.capitalize()
    get_current_language = translation.get_language()
    return render(request, "index.html", {
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
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full-name']
            user_name = form.cleaned_data['user-name']
            password = form.cleaned_data['password']
        else:
            form = SignupForm()

    return render(request, 'index.html')
