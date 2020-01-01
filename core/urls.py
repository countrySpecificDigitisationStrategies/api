from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Digitisation Strategies',
        default_version='1.0.0',
        description='This API allows you to create country specific digitisation strategies.',
    ),
    public=True,
    permission_classes=[],
    authentication_classes=[]
)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls')),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += staticfiles_urlpatterns()
