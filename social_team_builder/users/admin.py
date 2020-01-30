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

    # 4.7 Override the fieldsets to remove reference to `username`
    # (the `fieldsets` is for viewing/editing a user, the
    #  `add_fieldsets` is for ading a new user from the admin panel)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2',)}),
    )


admin.site.register(STBUser, STBUserAdmin)
