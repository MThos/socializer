from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(min_length=1, max_length=150, required=True, error_messages={'required': '* email is required'})
    full_name = forms.CharField(min_length=1, max_length=150, required=True, error_messages={'required': '* full name is required'})
    user_name = forms.CharField(min_length=1, max_length=150, required=True, error_messages={'required': '* user name is required'})
    password = forms.CharField(widget=forms.PasswordInput(), required=True, error_messages={'required': '* password is required'})
