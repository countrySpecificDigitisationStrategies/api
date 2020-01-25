from django.contrib import admin

from api.models import StrategyComment


@admin.register(StrategyComment)
class StrategyCommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy_thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'strategy_thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy_thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
