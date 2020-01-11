from django.contrib import admin

from api.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'thread', 'created', 'updated']
    search_fields = ['description']
    list_filter = ['user', 'thread']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'user',
                'thread',
                'parent',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
