from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('password-strength-checker/', views.PasswordStrengthCheckerView.as_view(), name="password-strength-checker"),
    # path('get-token/', views.GetAPITokenView.as_view(), name="get-token"),
    path('get-token/', obtain_auth_token, name="get-token"),
    path('signup/', views.UserSignupView.as_view(), name="signup"),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Password Strength Checker API",
        default_version='v1',
        description="API documentation for Password Strength Checker API",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-docs"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]
