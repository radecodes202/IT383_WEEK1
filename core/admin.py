from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Asset

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Asset)

