from django.contrib import admin

from api.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = ['name', 'created', 'updated']
    search_fields = ['name', 'created', 'updated']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'name',
                'flag_circle',
                'flag_rectangle',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
