# Details of 4.4 from Custom User Model Implementation
# (see users.models for full outline)
#
# We need to do this because Admin is highly coupled to the default User model
#
# Details of 4.7 from Custom User Model Implementation
# We need to provide customisations to ensure we only see email and not
# username
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import STBUserChangeForm, STBUserCreationForm
from users.models import STBUser


class STBUserAdmin(UserAdmin):
    add_form = STBUserCreationForm
    form = STBUserChangeForm
    model = STBUser

    # 4.7 remove 'username'
    list_display = ['email', 'first_name', 'last_name',]

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(STBUser, STBUserAdmin)