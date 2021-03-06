from django.conf.urls.static import static
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenRefreshView,)
from application import settings
from dvadmin.system.views.login import LoginView, CaptchaView, ApiLogin, LogoutView
from dvadmin.utils.swagger import CustomOpenAPISchemaGenerator
from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomOpenAPISchemaGenerator,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/system/', include('dvadmin.system.urls')),
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/captcha/', CaptchaView.as_view()),
    path('apiLogin/', ApiLogin.as_view()),
    path('api/', include('course.urls')),
    path('api/', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
