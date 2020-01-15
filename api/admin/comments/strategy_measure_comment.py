from django.contrib import admin

from api.models import StrategyMeasureComment


@admin.register(StrategyMeasureComment)
class StrategyMeasureCommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy_measure_thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'strategy_measure_thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy_measure_thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
