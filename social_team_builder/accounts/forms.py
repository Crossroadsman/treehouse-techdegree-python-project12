from django import forms

from accounts.models import UserProfile, Skill


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'name',
            'bio',
        )


class AvatarForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'avatar',
        )


# Use modelformset(factory?) to create the stacked formsets
# for skills and projects
