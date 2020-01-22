# Details of 4.4 from Custom User Model Implementation
# (see users.models for full outline)
#
# We need to do this because Admin is highly coupled to the default User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import STBUserChangeForm, STBUserCreationForm
from users.models import STBUser


class STBUserAdmin(UserAdmin):
    add_form = STBUserCreationForm
    form = STBUserChangeForm
    model = STBUser
    list_display = ['username', 'email', 'first_name', 'last_name',]


admin.site.register(STBUser, STBUserAdmin)