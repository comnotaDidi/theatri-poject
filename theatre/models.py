from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)


class TheatreHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

class Performance(models.Model):
    title = models.CharField(max_length=200)
    show_time = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)



class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('purchased', 'Purchased'),
    ]

    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Ticket for {self.performance.play.title} - Row {self.row} Seat {self.seat} ({self.status})"

