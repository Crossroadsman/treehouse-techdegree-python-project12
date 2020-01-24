"""social_team_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Details of 10.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - include users.urls
# - include django.contrib.auth.urls
#
# Note, because the URL routing is based on finding the first match in the
# patterns list, we can override any builtins by putting our same-named
# routes before the builtins. In this case, Django will check `users.urls`
# for url matches, only if it fails to find a match will it fall back
# to `django.contrib.auth.urls`

from django.urls import re_path

from . import views


app_name = 'app'
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^applications', views.applications, name="applications"),
]
