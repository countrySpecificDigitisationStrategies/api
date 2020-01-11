from django.contrib import admin

from api.models import Situation


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):

    list_display = ['situation_category', 'title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['situation_category']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'situation_category',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
