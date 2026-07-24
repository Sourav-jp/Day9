from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SignupAPIView

urlpatterns = [
    # Signup
    path("signup/", SignupAPIView.as_view(), name="signup"),

    # Login
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # Refresh Token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]