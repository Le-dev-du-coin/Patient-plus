from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import Account


class RegisterForm(UserCreationForm):
    """Form for User registration"""

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control floating"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control floating"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control floating"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control floating"})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control floating"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control floating"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control floating"})
    )

    class Meta:
        model = Account  # Get the default user model
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = "Votre mot de passe est faible"
