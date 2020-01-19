from django.contrib import admin

from api.models import BuildingBlockComment


@admin.register(BuildingBlockComment)
class BuildingBlockCommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'building_block_thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'building_block_thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'building_block_thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
