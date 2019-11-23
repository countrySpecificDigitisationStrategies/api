from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import User, Token, EmailConfirmation, PasswordReset


@admin.register(User)
class User(UserAdmin):
    model = User

    list_display = ['email', 'country', 'firstname', 'lastname', 'is_active', 'created', 'updated']
    search_fields = ['email', 'country', 'firstname', 'lastname', 'created', 'updated']
    ordering = []

    fieldsets = (
        (None, {
            'fields': [
                'email' 'country', 'firstname', 'lastname',
                'is_admin', 'is_representative', 'is_moderator',
                'is_active', 'is_staff', 'is_superuser',
                'last_login', 'password',
                'created', 'updated'
            ]
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': [
                'email' 'country', 'firstname', 'lastname',
                'is_admin', 'is_representative', 'is_moderator',
                'is_active',
                'password1', 'password2'
            ]
        }),
    )


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created', 'updated']
    #search_fields = ['user__email', 'code', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']


@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created', 'updated']
    #search_fields = ['user__email', 'code', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']


@admin.register(PasswordReset)
class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created', 'updated']
    #search_fields = ['user__email', 'code', 'created', 'updated']
    #list_filter = ['user', 'created', 'updated']
