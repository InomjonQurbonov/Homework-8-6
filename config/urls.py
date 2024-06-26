from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

...

schema_view = get_schema_view(
    openapi.Info(
        title="TMSITI WEB SITE",
        default_version='v1',
        description="TMSITI WEB SITE in Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="inomjonqurbonnov916@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # swagger
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # token
    path('token/api', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/api', TokenRefreshView.as_view(), name='token_refresh'),
    # my_apps
    path('news/', include('app_news.urls')),
    path('leadership/', include('app_leadership.urls')),
    path('standards/', include('app_standards.urls')),
    path('user/', include('user.urls')),
    path('regulations/', include('regulations.urls')),
    path('dictionary/', include('app_dictionary.urls')),
    path('shnk/', include('shnk_app.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
