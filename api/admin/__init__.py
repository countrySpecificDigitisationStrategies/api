from django.contrib import admin

from api.admin.analysis import AnalysisAdmin
from api.admin.building_block import BuildingBlockAdmin
from api.admin.country import CountryAdmin
from api.admin.measure import MeasureAdmin
from api.admin.strategy import StrategyAdmin
from api.admin.user import *
from api.admin.situation_category import SituationCategoryAdmin
from api.admin.situation import SituationAdmin

from api.admin.threads.strategy_measure_thread import StrategyMeasureThreadAdmin
from api.admin.comments.strategy_measure_comment import StrategyMeasureCommentAdmin

admin.site.site_header = 'SysDev'
admin.site.site_title = 'SysDev'
admin.site.site_url = None
admin.site.index_title = 'SysDev'
