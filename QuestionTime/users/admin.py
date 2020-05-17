from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """ In case you want to add other custom fields to the CustomUser model, you need to specify add_form, and form where
    add_form = where you can define a custom form class to create new users
    form = a form class to update the new instances
    """
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
