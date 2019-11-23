from django.contrib import admin

from api.models import Strategy, StrategyMeasureInformation


class StrategyMeasureInformationInline(admin.TabularInline):
    model = StrategyMeasureInformation
    extra = 0


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):

    list_display = ['user', 'title', 'is_published', 'created', 'updated']
    search_fields = ['title', 'description', 'created', 'updated']

    inlines = [StrategyMeasureInformationInline]
