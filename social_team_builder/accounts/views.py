from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404


User = get_user_model()


def profile(request):
    # user = get_object_or_404(User, pk=request.user.pk)

    # if hasattr(user, 'profile'):
    #     profile = user.profile
    # else:
    #     profile = None

    # # etc

    template = 'accounts/profile.html'
    context = {'selected': 'profile'}
    return render(request, template, context)
