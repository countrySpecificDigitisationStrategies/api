from django.contrib import admin

from api.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = ['name', 'is_developing_country', 'created', 'updated']
    search_fields = ['name', 'is_developing_country', 'created', 'updated']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'name',
                'flag',
                'flag_circle',
                'flag_rectangle',
                'is_developing_country',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']
