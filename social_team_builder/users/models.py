# See also (especially re reasons behind `AbstractBaseUser` vs 
# `AbstractUser`):
# https://wsvincent.com/django-custom-user-model-tutorial/
#
# This creates a custom user that is almost identical to the default user
# except it uses email as the string representation.
#
# The sequence is:
#
# (note, we can run the Django server before this process is complete, we just
# mustn't create or run migrations)
#
# 1. Create the Django Project
# 2. Create a `users` app
# 3. Decide whether to subclass `AbstractUser` or `AbstractBaseUser`
#    (this project uses the former, which is much, much easier)
# 4. Create initial custom user model:
#    4.1 update `settings.py` (see `settings.py` for more details)
#    4.2 create a replacement `User` model (see below)
#    4.3 create new user forms (see `forms.py`)
#    4.4 customise Django admin (see `admin.py`)
# 5. Run `makemigrations` for `users`
# 6. Run `migrate` for `users`
# 7. Create a superuser
# 8. Update settings.py for templates (see `settings.py` for details)
# 9. Create the project-level templates (see the templates for details):
#    9.1 `base.html` (or `_layout.html`)
#    9.2 `registration/login.html`
#    9.3 `home.html`
#    9.4 `signup.html`
# 10. Create URL routing:
#    10.1 `<project_dir>/<project_dir>/urls.py`
#    10.2 `users/urls.py`
# 11. Create views:
#    11.1 `users/views.py`
#
# To customise the user model to use email instead of username, before
# step 5:
#
# 4.5 Create a custom UserManager in `managers.py`
# 4.6 Update the model to reference the custom manager
# 4.7 Tweak the Admin to reflect the use of email instead of username
# 4.8 Edit the user create/change forms to reflect use of email
#
#
# Referencing the Custom User Model
# ---------------------------------
# See generally: https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#referencing-the-user-model
#
# Either:
# - `get_user_model()` (from `django.contrib.auth`); or
# - `settings.AUTH_USER_MODEL` (`from django.conf import settings`).
#
# Use the latter when:
# - defining FK/MTM relations in models;
# - connecting to signals sent by the user model
#
# Apparently (see https://wsvincent.com/django-referencing-the-user-model/),
# since v1.11, we can now use `get_user_model` anywhere we once needed to use
# AUTH_USER_MODEL (but note that the statements above re using AUTH_USER_MODEL
# come directly from the Django 2.2 docs).
# `get_user_model` is preferable where available because apparently, it will 
# work whether the installed user model is built-in or custom. 
# `AUTH_USER_MODEL` only works for custom models.
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import STBUserManager


class STBUser(AbstractUser):

    # override username to eliminate it as a field
    username = None
    
    # override email to make it required and unique
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    # the following is an attribute not a field
    objects = STBUserManager()
    
    # the following attribute specifies which of our fields should be the
    # unique identifier for users. In this case, based on our selections above
    # either `email` or `username` could be valid choices for this attribute
    USERNAME_FIELD = 'email'

    # the following is a list of fields that are passed through to the
    # create_superuser method (other than USERNAME_FIELD and password)
    # when using (e.g.) `python3 manage.py createsuperuser`
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        # Note that AbstractUser has built-in name fields but
        # we want the User objet to only be responsible for
        # uniquely identifying a particular user, all user-facing
        # metadata (e.g., name) should be part of the UserProfile
        # object.
        return self.email
