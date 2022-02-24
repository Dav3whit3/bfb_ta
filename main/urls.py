"""bfb_ta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from django.contrib.auth.decorators import login_required

from apps.mentors import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    permission_classes=[permissions.IsAdminUser],
)

router = routers.DefaultRouter()
router.register(r'mentors', views.MentorViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'mentorship', views.MentorshipViewSet)


urlpatterns = [

    # Wrap with login required when the login interface is completed
    # path('', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),                                       
    # path('redoc', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),                                       
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
