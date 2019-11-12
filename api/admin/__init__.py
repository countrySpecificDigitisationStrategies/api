from django.contrib import admin

from api.admin.building_block import BuildingBlockAdmin
from api.admin.measure import MeasureAdmin
from api.admin.user import *

admin.site.site_header = 'SysDev'
admin.site.site_title = 'SysDev'
admin.site.site_url = None
admin.site.index_title = 'SysDev'
