from django.contrib import admin
from django.contrib.auth.models import User
from . models import *
# Register your models here.

admin.site.register(User)
#admin.site.register(Additionally_Filed_User)
admin.site.register(Seeker_Education)
admin.site.register(Seeker_Personal_Information)
admin.site.register(Seeker_Professional_Information)