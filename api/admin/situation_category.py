from django.contrib import admin

from api.models import SituationCategory


@admin.register(SituationCategory)
class SituationCategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'goal_title', 'created', 'updated']
    search_fields = ['title', 'description', 'goal_title', 'goal_description', 'created', 'updated']
    list_filter = ['building_block']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'building_block',
                'title',
                'description',
                'goal_title',
                'goal_description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
