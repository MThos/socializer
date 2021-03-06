import datetime

from django.shortcuts import render, redirect
from django.urls import resolve
from django.utils import translation

from .forms import SignupForm
from .models import User


def index(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'],
            full_name = form.cleaned_data['full_name'],
            user_name = form.cleaned_data['user_name'],
            password = form.cleaned_data['password']

            if User.objects.filter(email=email).exists():
                email_unique = False
            else:
                email_unique = True

            if User.objects.filter(user_name=user_name).exists():
                raise ValidationError("user name already exists")
            else:
                user_name_unique = True

            if email_unique and user_name_unique:
                user = User(email=email, full_name=full_name, user_name=user_name, password=password, signup=datetime.datetime.now(), logins=0, last_login=datetime.datetime.now())
                user.save()
                signed_up = "You are now signed up, " + full_name[0] + "."

                return render(request, "registration/signup.html", {
                    "signed_up": signed_up,
                    "full_name": full_name
                })
        else:
            year = datetime.datetime.now().year
            # title = resolve(request.path).app_name.capitalize()
            get_current_language = translation.get_language()
            return render(request, "registration/index.html", {
                "year": year,
                "title": "Sign up",
                "tab_title": "Sign up - Socializer",
                "sub_title": "SOCIALIZER",
                "get_current_language": get_current_language,
                "form": form
            })
    else:
        year = datetime.datetime.now().year
        # title = resolve(request.path).app_name.capitalize()
        get_current_language = translation.get_language()
        return render(request, "registration/index.html", {
            "year": year,
            "title": "Sign up",
            "tab_title": "Sign up - Socializer",
            "sub_title": "SOCIALIZER",
            "get_current_language": get_current_language
        })
