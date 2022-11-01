from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views_api import RegisterView


urlpatterns = [
    # path('auth/', include('rest_framework.urls')),
    path('signup/', RegisterView.as_view(), name="signup"),
    path('signin/', TokenObtainPairView.as_view(), name="signin"),
    path('refresh/', TokenRefreshView.as_view(), name="refresh"),
]
