from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GroupViewSet, PermissionViewSet, register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"permissions", PermissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", register_user, name="register_user"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
