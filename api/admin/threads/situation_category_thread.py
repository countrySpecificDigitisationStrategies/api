from django.contrib import admin

from api.models import SituationCategoryThread


@admin.register(SituationCategoryThread)
class SituationCategoryThreadAdmin(admin.ModelAdmin):

    list_display = ['user', 'strategy', 'situation_category', 'title', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['user', 'strategy', 'situation_category']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'strategy',
                'situation_category',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
