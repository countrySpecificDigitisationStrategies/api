from django.contrib import admin

from api.models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):

    list_display = ['country', 'title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['country']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'country',
                'title',
                'description',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
