from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(min_length=1, max_length=150, required=True)
    full_name = forms.CharField(min_length=1, max_length=150, required=True)
    user_name = forms.CharField(min_length=1, max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
