from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()

# Регистрируем API ViewSets
# router.register(r'actors', ActorViewSet)
# router.register(r'plays', PlayViewSet)
# router.register(r'halls', TheatreHallViewSet)
# router.register(r'performances', PerformanceViewSet)
# router.register(r'reservations', ReservationViewSet)
# router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Theatre API",
        default_version='v1',
        description="Документация для театрального API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('api/doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
