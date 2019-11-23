from django.contrib import admin

from api.models import Pillar


@admin.register(Pillar)
class PillarAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = []

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'title',
                'description',
                'image',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
