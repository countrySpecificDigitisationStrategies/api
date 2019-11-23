from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.resources import AuthViewSet, BuildingBlockViewSet, CommentViewSet, MeasureViewSet, PillarViewSet, UserViewSet, StrategyViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'building-blocks', BuildingBlockViewSet, base_name='building-blocks')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'measures', MeasureViewSet, base_name='measures')
router.register(r'pillars', PillarViewSet, base_name='pillars')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'strategies', StrategyViewSet, base_name='strategies')

urlpatterns = [
    url('', include(router.urls))
]
