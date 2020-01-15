from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.resources import AnalysisViewSet, AuthViewSet, BuildingBlockViewSet, StrategyMeasureCommentViewSet, CountryViewSet, MeasureViewSet, SituationCategoryViewSet, SituationViewSet, StrategyViewSet, StrategyMeasureViewSet, StrategyMeasureThreadViewSet, UserViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'users', UserViewSet, basename='users')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'analyses', AnalysisViewSet, basename='analyses')

router.register(r'building-blocks', BuildingBlockViewSet, basename='building-blocks')
router.register(r'situation-categories', SituationCategoryViewSet, basename='situation-categories')
router.register(r'situations', SituationViewSet, basename='situations')
router.register(r'measures', MeasureViewSet, basename='measures')
router.register(r'strategies', StrategyViewSet, basename='strategies')
router.register(r'strategy-measures', StrategyMeasureViewSet, basename='strategy-measures')

router.register(r'strategy-measure-threads', StrategyMeasureThreadViewSet, basename='strategy-measure-threads')
router.register(r'strategy-measure-comments', StrategyMeasureCommentViewSet, basename='strategy-measure-comments')

urlpatterns = [
    url('', include(router.urls))
]
