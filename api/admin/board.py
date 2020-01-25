from django.contrib import admin

from api.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):

    list_display = ['country', 'created', 'updated']
    search_fields = ['country__name', 'created', 'updated']
    list_filter = ['country']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'country',
                'users',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
