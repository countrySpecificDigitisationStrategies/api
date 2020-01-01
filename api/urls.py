"""
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.resources import AuthViewSet, BuildingBlockViewSet, CommentViewSet, CountryViewSet, GoalViewSet, MeasureViewSet, SituationViewSet, StrategyViewSet, UserViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'building-blocks', BuildingBlockViewSet, base_name='building-blocks')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'countries', CountryViewSet, base_name='countries')
router.register(r'goals', GoalViewSet, base_name='goals')
router.register(r'measures', MeasureViewSet, base_name='measures')
router.register(r'situations', SituationViewSet, base_name='situations')
router.register(r'strategies', StrategyViewSet, base_name='strategies')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    url('', include(router.urls))
]
"""


from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.resources import AuthViewSet, BuildingBlockViewSet, CommentViewSet, CountryViewSet, DiscussionViewSet, GoalViewSet, MeasureViewSet, SituationViewSet, StrategyViewSet, ThreadViewSet, UserViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register(r'auth', AuthViewSet, basename='auth')
default_router.register(r'users', UserViewSet, basename='users')
default_router.register(r'countries', CountryViewSet, basename='countries')
default_router.register(r'threads', ThreadViewSet, basename='threads')
default_router.register(r'comments', CommentViewSet, basename='comments')
default_router.register(r'discussion', DiscussionViewSet, basename='discussion')


router = routers.SimpleRouter()
router.register(r'strategies', StrategyViewSet)

building_blocks_router = routers.NestedSimpleRouter(router, r'strategies', lookup='strategy')
building_blocks_router.register(r'building-blocks', BuildingBlockViewSet)

situations_router = routers.NestedSimpleRouter(building_blocks_router, r'building-blocks', lookup='building_block')
situations_router.register(r'situations', SituationViewSet)

goals_router = routers.NestedSimpleRouter(situations_router, r'situations', lookup='situation')
goals_router.register(r'goals', GoalViewSet)

#strategy_measure_router = routers.NestedSimpleRouter(goals_router, r'goals', lookup='goal')
#strategy_measure_router.register(r'strategy-measures', StrategyMeasureViewSet)


urlpatterns = [
    url(r'^', include(default_router.urls)),
    url(r'^', include(router.urls)),
    url(r'^', include(building_blocks_router.urls)),
    url(r'^', include(situations_router.urls)),
    url(r'^', include(goals_router.urls)),
]
