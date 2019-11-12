from django.contrib import admin

from api.admin.building_block import BuildingBlockAdmin
from api.admin.comment import CommentAdmin
from api.admin.measure import MeasureAdmin
from api.admin.strategy import StrategyAdmin
from api.admin.user import *

admin.site.site_header = 'SysDev'
admin.site.site_title = 'SysDev'
admin.site.site_url = None
admin.site.index_title = 'SysDev'