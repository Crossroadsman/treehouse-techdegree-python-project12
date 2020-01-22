# Details of 4.3 from Custom User Model Implementation
# (see users.models for full outline)
#
# We're mostly just subclassing existing forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import STBUser


class STBUserCreationForm(UserCreationForm):

    class Meta:
        model = STBUser
        fields = ('username', 'email',)


class STBUserChangeForm(UserChangeForm):

    class Meta:
        model = STBUser
        fields = ('username', 'email',)