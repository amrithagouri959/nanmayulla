from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Row, Column, Submit, Reset
from crispy_forms.bootstrap import PrependedText


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "photo",
        ]
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "password": "Password",
            "confirm_password": "Confirm Password",
            "photo": "Profile Picture",
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            PrependedText("username", "@", placeholder="user_name"),
            Row(
                Column("password", css_class="form-group col"),
                Column("confirm_password", css_class="form-group col"),
                css_class="form-row",
            ),
            Row(
                Column("first_name", css_class="form-group col"),
                Column("last_name", css_class="form-group col"),
                css_class="form-row",
            ),
            "email",
            "photo",
            Submit("submit", "Register", css_class="btn btn-primary"),
            Reset("reset", "Reset", css_class="btn btn-secondary"),
        )

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        else:
            return confirm_password
