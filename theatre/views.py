from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Для отправки сообщений пользователю
from .models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket, Reservation
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
)
from django.views import View

def home(request):
    return render(request, 'theatre/home.html')

def plays(request):
    return render(request, 'theatre/plays.html')


# ViewSet для API
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Страница с деталями спектакля
class PerformanceDetailView(View):
    def get(self, request, performance_id):
        performance = get_object_or_404(Performance, pk=performance_id)
        available_tickets = performance.ticket_set.filter(status='available')
        return render(request, 'performance_detail.html', {
            'performance': performance,
            'available_tickets': available_tickets,
        })

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# Страница бронирования билетов
class BuyTicketView(View):
    def get(self, request, performance_id):
        performance = get_object_or_404(Performance, pk=performance_id)
        available_tickets = performance.ticket_set.filter(status='available')
        return render(request, 'buy_ticket.html', {
            'performance': performance,
            'available_tickets': available_tickets,
        })

    def post(self, request, performance_id):
        ticket_ids = request.POST.getlist('ticket_ids')
        performance = get_object_or_404(Performance, pk=performance_id)

        # Создаем бронирование для пользователя
        user = request.user
        reservation = Reservation.objects.create(user=user)

        # Бронирование билетов
        tickets = Ticket.objects.filter(id__in=ticket_ids, status='available', performance=performance)
        if tickets.exists():
            for ticket in tickets:
                ticket.status = 'reserved'
                ticket.reservation = reservation
                ticket.save()

            messages.success(request, f'Вы успешно забронировали билеты на спектакль "{performance.play.title}".')
            return redirect('ticket_confirmation', reservation_id=reservation.id)
        else:
            messages.error(request, 'Некоторые выбранные билеты уже забронированы или недоступны.')
            return redirect('performance_detail', performance_id=performance.id)

class ReservationListView(View):
    def get(self, request):
        # Получаем все бронирования для текущего пользователя
        reservations = Reservation.objects.filter(user=request.user)
        return render(request, 'reservations.html', {'reservations': reservations})


# Страница подтверждения бронирования
class TicketConfirmationView(View):
    def get(self, request, reservation_id):
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        return render(request, 'ticket_confirmation.html', {'reservation': reservation})

