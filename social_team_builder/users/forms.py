# Details of 4.3 from Custom User Model Implementation
# (see users.models for full outline)
#
# We're mostly just subclassing existing forms
#
# Details of 4.8 from Custom User Model Implementation
# - remove 'username' from fields tuple
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import STBUser


class STBUserCreationForm(UserCreationForm):

    class Meta:
        model = STBUser
        fields = ('email',)


class STBUserChangeForm(UserChangeForm):

    class Meta:
        model = STBUser
        fields = ('email',)
