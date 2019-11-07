from django.contrib import admin

from api.models import Measure


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
