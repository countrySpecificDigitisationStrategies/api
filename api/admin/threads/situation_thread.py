from django.contrib import admin

from api.models import SituationThread


@admin.register(SituationThread)
class SituationThreadAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy', 'situation', 'title', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['user', 'strategy', 'situation']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy',
                'situation',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
