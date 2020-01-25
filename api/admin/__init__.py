from django.contrib import admin

from api.admin.analysis import AnalysisAdmin
from api.admin.board import BoardAdmin
from api.admin.building_block import BuildingBlockAdmin
from api.admin.country import CountryAdmin
from api.admin.measure import MeasureAdmin
from api.admin.strategy import StrategyAdmin
from api.admin.user import *
from api.admin.situation_category import SituationCategoryAdmin
from api.admin.situation import SituationAdmin

from api.admin.comments.building_block_comment import BuildingBlockCommentAdmin
from api.admin.comments.situation_category_comment import SituationCategoryCommentAdmin
from api.admin.comments.situation_comment import SituationCommentAdmin
from api.admin.comments.strategy_measure_comment import StrategyMeasureCommentAdmin
from api.admin.comments.strategy_comment import StrategyCommentAdmin

from api.admin.threads.building_block_thread import BuildingBlockThreadAdmin
from api.admin.threads.situation_category_thread import SituationCategoryThreadAdmin
from api.admin.threads.situation_thread import SituationThreadAdmin
from api.admin.threads.strategy_measure_thread import StrategyMeasureThreadAdmin
from api.admin.threads.strategy_thread import StrategyThreadAdmin

admin.site.site_header = 'SysDev'
admin.site.site_title = 'SysDev'
admin.site.site_url = None
admin.site.index_title = 'SysDev'
