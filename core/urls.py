from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views.user_views import RegisterView
from .views.shortner_views import RedirectView, CreateShortURLView
from .views.analytics_views import AnalyticsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('shorten/', CreateShortURLView.as_view(), name='create-short-url'),
    path('r/<str:short_url>/', RedirectView.as_view(), name='redirect'),
    path('analytics/<str:short_url>/', AnalyticsView.as_view(), name='analytics'),
] 