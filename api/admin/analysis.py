from django.contrib import admin

from api.models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):

    list_display = ['created', 'updated']
    search_fields = ['created', 'updated']

