from django.contrib import admin

from api.models import Strategy


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_published', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
