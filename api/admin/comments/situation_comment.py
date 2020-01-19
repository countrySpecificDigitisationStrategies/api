from django.contrib import admin

from api.models import SituationComment


@admin.register(SituationComment)
class SituationCommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'situation_thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'situation_thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'situation_thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
