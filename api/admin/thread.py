from django.contrib import admin

from api.models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy_measure', 'title', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['user', 'strategy_measure']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy_measure',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
