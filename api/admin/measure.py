from django.contrib import admin

from api.models import Measure


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):

    list_display = ['goal', 'title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['goal']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'goal',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
