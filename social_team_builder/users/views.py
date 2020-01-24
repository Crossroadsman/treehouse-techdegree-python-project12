# Details of 11.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - create SignUp view GCBV

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

from users.forms import STBUserCreationForm


class SignUpView(generic.CreateView):
    form_class = STBUserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'signup.html'


class SignInView(LoginView):
    template_name = 'registration/signin.html'
