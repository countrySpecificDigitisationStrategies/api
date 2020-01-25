from django.contrib import admin

from api.models import StrategyThread


@admin.register(StrategyThread)
class StrategyThreadAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy', 'title', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['user', 'strategy']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
