from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.resources import AuthViewSet, UserViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    url('', include(router.urls))
]
