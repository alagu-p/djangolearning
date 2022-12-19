# from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
# Register your models here.
from core.models import User


class SuperUser(UserAdmin):
    ordering = ['id']


admin.site.register(User, SuperUser)
