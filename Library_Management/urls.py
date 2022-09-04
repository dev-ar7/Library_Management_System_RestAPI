from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_sliding
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view 

schema_view = get_schema_view(
    openapi.Info(
        title='Library API',
        default_version='v1',
        description='Official API documentation of Library Management System',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="arnab.gupta.ar7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('librarian/', admin.site.urls),
    path('api/v1/',
            include([
                path('auth/', include('user.urls')),
                path('token_auth/', token_obtain_sliding),
                path('library/', include('books.urls')),
                path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
            ])
    )
]
