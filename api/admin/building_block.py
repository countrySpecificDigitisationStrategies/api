from django.contrib import admin

from api.models import BuildingBlock


@admin.register(BuildingBlock)
class BuildingBlockAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
