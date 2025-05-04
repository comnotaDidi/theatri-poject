from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import PerformanceDetailView, BuyTicketView, TicketConfirmationView, GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet, PerformanceViewSet, ReservationViewSet, TicketViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Создаем роутеры для API
router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'plays', PlayViewSet)
router.register(r'halls', TheatreHallViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    
    # Страница всех спектаклей
    path('plays/', views.plays, name='plays'),

    # Страница с деталями спектакля
    path('performance/<int:performance_id>/', PerformanceDetailView.as_view(), name='performance_detail'),
    
    # Страница бронирования билетов
    path('buy_ticket/<int:performance_id>/', BuyTicketView.as_view(), name='buy_ticket'),
    
    # Страница подтверждения бронирования билетов
    path('ticket_confirmation/<int:reservation_id>/', TicketConfirmationView.as_view(), name='ticket_confirmation'),

    # Страница с бронированиями
    path('reservations/', views.ReservationListView.as_view(), name='reservations'),

    # API для всех зарегистрированных ViewSets
    path('api/', include(router.urls)),

    # Аутентификация через JWT (для получения токенов)
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

# в urlpatterns:
path('api/doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
