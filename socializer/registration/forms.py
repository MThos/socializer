from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True)
    full_name = forms.CharField(max_length=150, required=True)
    user_name = forms.CharField(max_length=150, required=True)
    password = forms.PasswordInput()
