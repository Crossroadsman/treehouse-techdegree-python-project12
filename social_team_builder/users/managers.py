# Details of 4.5 from Custom User Model Implementation
# (see users.models for full outline)
#
# We only need to do this if we are changing the required fields of
# the user (e.g., here using email as the username)
from django.contrib.auth.models import BaseUserManager


class STBUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """Creates and saves a user with the specified email and password"""
        if not email:
            raise ValueError("Users must provide an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
