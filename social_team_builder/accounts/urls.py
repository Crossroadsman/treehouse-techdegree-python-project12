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

from django.urls import re_path

from . import views


app_name = 'accounts'
urlpatterns = [
    re_path(r'profile$', views.profile, name='profile'),
    re_path(r'profile_edit$', views.profile_edit, name='profile_edit'),
    re_path(r'avatar_add$', views.avatar_add, name='avatar_add'),
]
