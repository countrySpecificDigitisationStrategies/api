from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.resources import AuthViewSet, BuildingBlockViewSet, CommentViewSet, GoalViewSet, MeasureViewSet, SituationViewSet, StrategyViewSet, UserViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'building-blocks', BuildingBlockViewSet, base_name='building-blocks')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'goals', GoalViewSet, base_name='goals')
router.register(r'measures', MeasureViewSet, base_name='measures')
router.register(r'situations', SituationViewSet, base_name='situations')
router.register(r'strategies', StrategyViewSet, base_name='strategies')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    url('', include(router.urls))
]
