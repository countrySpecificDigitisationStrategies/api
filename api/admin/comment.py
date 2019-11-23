from django.contrib import admin

from api.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated']
    search_fields = ['description', 'created', 'updated']
