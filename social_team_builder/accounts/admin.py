from django.contrib import admin


from accounts.models import UserProfile, Skill

admin.site.register(UserProfile)
admin.site.register(Skill)
