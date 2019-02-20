from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Editing the user creation form
    """

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        """
        Add first_name, last_name and email in the registration form
        """
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
