from django.contrib import admin

from api.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
