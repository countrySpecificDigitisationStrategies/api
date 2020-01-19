from django.contrib import admin

from api.models import BuildingBlockThread


@admin.register(BuildingBlockThread)
class BuildingBlockThreadAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy', 'building_block', 'title', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['user', 'strategy', 'building_block']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy',
                'building_block',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
