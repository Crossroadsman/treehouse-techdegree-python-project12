from django import forms

from accounts.models import UserProfile, Skill


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Full Name',
            'class': 'circle--input--h1',
        })

        self.fields['bio'].widget.attrs.update({
            'placeholder': 'Tell us about yourself...',
        })

    class Meta:
        model = UserProfile
        fields = (
            'name',
            'bio',
        )


class AvatarForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['avatar'].widget.attrs.update({
            'class': 'button',
        })

    class Meta:
        model = UserProfile
        fields = (
            'avatar',
        )


# Use modelformset(factory?) to create the stacked formsets
# for skills and projects
