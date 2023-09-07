from django import forms


class LoginValidationForm(forms.Form):
    account = forms.CharField(required=True)
    login_auth = forms.CharField(required=True)
    third = forms.CharField(required=False)