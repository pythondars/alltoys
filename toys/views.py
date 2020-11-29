from django.shortcuts import render
from django.utils import timezone

from toys.models import Toy


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"welcome_text": "Welcome to Alltoys!"})


def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    return render(request, "toys/toys.html", context={"toys": toys})
