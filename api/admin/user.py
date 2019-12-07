from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import User, Token, EmailConfirmation, PasswordReset


class EmailConfirmationInline(admin.TabularInline):
    model = EmailConfirmation

    def has_add_permission(self, request):
        return False


class PasswordResetInline(admin.TabularInline):
    model = PasswordReset

    def has_add_permission(self, request):
        return False


class TokenAdminInline(admin.TabularInline):
    model = Token

    def has_add_permission(self, request):
        return False


@admin.register(User)
class User(UserAdmin):
    model = User

    list_display = ['email', 'country', 'firstname', 'lastname', 'current_country', 'is_active', 'created', 'updated']
    search_fields = ['email', 'country', 'firstname', 'lastname', 'current_country', 'created', 'updated']
    list_filter = []
    ordering = []

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'email', 'country', 'firstname', 'lastname', 'current_country',
                'is_admin', 'is_representative', 'is_moderator',
                'last_login', 'password',
                'created', 'updated'
            ]
        }]
    ]

    add_fieldsets = (
        (None, {
            'fields': [
                'email', 'country', 'firstname', 'lastname', 'current_country',
                'is_admin', 'is_representative', 'is_moderator',
                'password1', 'password2'
            ]
        }),
    )

    readonly_fields = ['id', 'created', 'updated']

    inlines = [EmailConfirmationInline, PasswordResetInline, TokenAdminInline]
