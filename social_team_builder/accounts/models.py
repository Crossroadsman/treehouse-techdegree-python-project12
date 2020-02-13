from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=True)

    # Consider changing to RichTextField
    bio = models.TextField()

    avatar = models.ImageField(
        upload_to='avatars',
        blank=True,
        null=True
    )

    # skills: MTM relationship defined on other side
    # projects = TODO

    def __str__(self):
        if len(self.name) > 0:
            return self.name
        else:
            return str(self.user)

    def get_absolute_url(self):
        return reverse('accounts:profile')


class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    users = models.ManyToManyField(
        UserProfile,
        
    )

    # TODO
    # projects = models.ManyToManyField()

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name