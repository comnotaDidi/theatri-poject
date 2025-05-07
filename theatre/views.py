from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Performance, Ticket
from .serializers import ActorSerializer
from rest_framework import viewsets
from rest_framework import viewsets
from .models import Actor
from django.views import View

# Главная страница
def home(request):
    return render(request, 'theatre/home.html')
