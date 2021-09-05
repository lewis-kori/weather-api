from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()
admin.site.register(User, UserAdmin)

admin.site.site_header = 'Weather API dashboard'
admin.site.site_title = 'Weather API'
