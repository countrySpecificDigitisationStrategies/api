from django.contrib import admin

from api.models import Situation


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['building_block']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'building_block',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
