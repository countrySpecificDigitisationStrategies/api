from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Sysdev API',
        default_version='v1',
        description='Sysdev API description',
        # terms_of_service='https://www.google.com/policies/terms/',
        # contact=openapi.Contact(email='contact@snippets.local'),
        #license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[],
    authentication_classes=[],
)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls')),

    #url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += staticfiles_urlpatterns()
