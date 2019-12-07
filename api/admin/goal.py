from django.contrib import admin

from api.models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['situation']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'situation',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
