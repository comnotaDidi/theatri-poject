from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'plays', PlayViewSet)
router.register(r'halls', TheatreHallViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('plays/', views.plays, name='plays'),
    path('api/', include(router.urls)),
]
