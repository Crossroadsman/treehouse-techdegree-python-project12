from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from accounts.forms import UserProfileForm, AvatarForm


User = get_user_model()


def profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if not hasattr(user, 'userprofile'):
        return redirect(reverse('accounts:profile_edit'))

    profile = user.userprofile
    template = 'accounts/profile.html'
    context = {
        'selected': 'profile',
        'profile': profile,
    }
    return render(request, template, context)


def profile_edit(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if hasattr(user, 'userprofile'):
        up_instance = user.userprofile
    else:
        up_instance = None

    if request.method == 'POST':
        up_form = UserProfileForm(
            request.POST,
            instance=up_instance
        )
        a_form = AvatarForm(
            request.FILES,
            instance=up_instance
        )
        if all([up_form.is_valid(),
                a_form.is_valid()]):
            profile = up_form.save(commit=False)
            profile.user = user
            # sanitize html/markdown here
            # (see e.g., https://github.com/Crossroadsman/treehouse-techdegree-python-project7/blob/master/accounts/views.py)
            profile.save()
            a_form.save()
            return redirect(reverse('accounts:profile'))

    else:  # GET
        up_form = UserProfileForm(instance=up_instance)
        a_form = AvatarForm(instance=up_instance)

    template = 'accounts/profile_edit.html'
    context = {
        'selected': 'profile',
        'up_form': up_form,
        'a_form': a_form,
    }
    return render(request, template, context)
