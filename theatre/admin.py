from django.contrib import admin
from .models import (
    Genre, Actor, Play, TheatreHall,
    Performance, Reservation, Ticket
)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    filter_horizontal = ('genres', 'actors')

@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rows', 'seats_in_row')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_time', 'category')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'row', 'seat', 'performance', 'reservation')
