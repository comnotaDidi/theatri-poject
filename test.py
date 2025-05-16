from django.test import TestCase
from django.contrib.auth.models import User
from .models import Actor, Genre, Play, TheatreHall, Performance, Reservation, Ticket
from django.utils import timezone

class ActorModelTest(TestCase):
    def test_actor_creation(self):
        # Create an actor
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        
        # Test the field values
        self.assertEqual(actor.first_name, "John")
        self.assertEqual(actor.last_name, "Doe")
        
        # Test the string representation
        self.assertEqual(str(actor), "John Doe")

class PerformanceModelTest(TestCase):
    def test_performance_creation(self):
        # Create necessary related models
        actor = Actor.objects.create(first_name="Jane", last_name="Doe")
        genre = Genre.objects.create(name="Comedy")
        play = Play.objects.create(title="Funny Play", description="A really funny play")
        play.genres.add(genre)
        play.actors.add(actor)

        theatre_hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=20)

        # Create a performance
        performance = Performance.objects.create(play=play, theatre_hall=theatre_hall, show_time=timezone.now())

        # Test the field values
        self.assertEqual(performance.play.title, "Funny Play")
        self.assertEqual(performance.theatre_hall.name, "Main Hall")
        
        # Test the instance type
        self.assertTrue(isinstance(performance, Performance))

class ReservationModelTest(TestCase):
    def test_reservation_creation(self):
        # Create a user and a reservation
        user = User.objects.create_user(username="testuser", password="password123")
        reservation = Reservation.objects.create(user=user)
        
        # Test the user associated with the reservation
        self.assertEqual(reservation.user.username, "testuser")
        
        # Test the instance type
        self.assertTrue(isinstance(reservation, Reservation))

class TicketModelTest(TestCase):
    def test_ticket_creation(self):
        # Create necessary related models
        user = User.objects.create_user(username="testuser", password="password123")
        genre = Genre.objects.create(name="Action")
        actor = Actor.objects.create(first_name="Tom", last_name="Cruise")
        play = Play.objects.create(title="Action Play", description="An action-packed play")
        play.genres.add(genre)
        play.actors.add(actor)

        theatre_hall = TheatreHall.objects.create(name="Action Hall", rows=10, seats_in_row=20)
        performance = Performance.objects.create(play=play, theatre_hall=theatre_hall, show_time=timezone.now())

        # Create a ticket for the performance
        ticket = Ticket.objects.create(row=1, seat=1, performance=performance, status="available", price=10.50)

        # Test the field values
        self.assertEqual(ticket.row, 1)
        self.assertEqual(ticket.seat, 1)
        self.assertEqual(ticket.performance.play.title, "Action Play")
        self.assertEqual(ticket.status, "available")
        self.assertEqual(ticket.price, 10.50)
        
        # Test the string representation
        self.assertEqual(str(ticket), "Ticket for Action Play - Row 1 Seat 1 (available)")
