from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import User, Token, EmailConfirmation, PasswordReset


@admin.register(User)
class User(UserAdmin):
    model = User

    list_display = ['email', 'firstname', 'lastname', 'is_active', 'created', 'updated']
    search_fields = ['email', 'firstname', 'lastname', 'created', 'updated']
    ordering = []

    fieldsets = (
        (None, {
            'fields': ('email', 'firstname', 'lastname', 'is_active', 'groups', 'last_login', 'password')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'firstname', 'lastname', 'is_active', 'password1', 'password2')}
         ),
    )


"""
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'identifier', 'created', 'updated']
    #search_fields = ['user__email', 'identifier', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']


@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ['user', 'identifier', 'created', 'updated']
    #search_fields = ['user__email', 'identifier', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']


@admin.register(PasswordReset)
class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ['user', 'identifier', 'created', 'updated']
    #search_fields = ['user__email', 'identifier', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']
"""
