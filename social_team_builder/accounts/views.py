import logging

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

    logging.debug(f'Loaded user: {user} from request')

    if hasattr(user, 'userprofile'):
        logging.debug(f'{user} has an existing userprofile')
        up_instance = user.userprofile
    else:
        logging.debug(f'{user} DOES NOT have an existing userprofile')
        up_instance = None

    if request.method == 'POST':
        logging.debug('method is POST')
        up_form = UserProfileForm(
            request.POST,
            instance=up_instance
        )
        if up_form.is_valid():

            logging.debug('form passed validation')
            
            # User Profile
            logging.debug('saving form (commit=False)')
            profile = up_form.save(commit=False)
            logging.debug('linking user to profile')
            profile.user = user
            # sanitize html/markdown here
            # (see e.g., https://github.com/Crossroadsman/treehouse-techdegree-python-project7/blob/master/accounts/views.py)
            logging.debug(f'{profile.user}')

            # WOULD THE RESULT BE ANY DIFFERENT IF WE EXPLICITLY
            # SET profile.user TO request.user INSTEAD OF user?
            logging.debug('saving up form (commit=True)')
            profile.save()
            
            logging.debug('redirecting')
            return redirect(reverse('accounts:profile'))

        else:
            # CONSIDER DELETING THIS BLOCK ONCE EVERYTHING WORKS
            logging.debug(up_form.errors)  # includeds non-field errors

            # will need this when we re-render the view
            a_form = AvatarForm(instance=up_instance)

    else:  # GET
        logging.debug('method is GET')
        up_form = UserProfileForm(instance=up_instance)
        a_form = AvatarForm(instance=up_instance)

    template = 'accounts/profile_edit.html'
    context = {
        'selected': 'profile',
        'up_form': up_form,
        'a_form': a_form,
    }
    return render(request, template, context)


def avatar_add(request):
    user = get_object_or_404(User, pk=request.user.pk)

    logging.debug(f'Loaded user: {user} from request')

    if hasattr(user, 'userprofile'):
        logging.debug(f'{user} has an existing userprofile')
        up_instance = user.userprofile
    else:
        logging.debug(f'{user} DOES NOT have an existing userprofile')
        up_instance = None

    if request.method == 'POST':
        logging.debug('method is POST')
        a_form = AvatarForm(
            request.FILES,
            instance=up_instance
        )
        if a_form.is_valid():

            logging.debug('form passed validation')
            
            logging.debug('saving form (commit=False)')
            profile = a_form.save(commit=False)
            logging.debug('linking user to profile')
            profile.user = user

            logging.debug(f'{profile.user}')

            logging.debug('saving up form (commit=True)')
            profile.save()
            
            logging.debug('redirecting')
            return redirect(reverse('accounts:profile'))

        else:
            # CONSIDER DELETING THIS BLOCK ONCE EVERYTHING WORKS
            logging.debug(a_form.errors)
            return redirect(reverse('accounts:profile_edit'))

    else:  # GET
        logging.debug('method is GET')
    
    return redirect(reverse('accounts:profile'))

