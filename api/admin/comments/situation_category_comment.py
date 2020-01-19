from django.contrib import admin

from api.models import SituationCategoryComment


@admin.register(SituationCategoryComment)
class SituationCategoryCommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'situation_category_thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'situation_category_thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'situation_category_thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
