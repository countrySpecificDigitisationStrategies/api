from django.contrib import admin

from api.models import Strategy, StrategyMeasure


class StrategyMeasureInline(admin.TabularInline):

    model = StrategyMeasure
    extra = 0


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):

    list_display = ['board', 'title', 'is_published', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']
    list_filter = ['board']

    fieldsets = [
        [None, {
            'fields': [
                'id',
                'board',
                'title',
                'description',
                'is_published',
                'created',
                'updated'
            ]
        }]
    ]

    readonly_fields = ['id', 'created', 'updated']

    inlines = [StrategyMeasureInline]
