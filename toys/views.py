from django.shortcuts import render

from toys.models import Toy


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"welcome_text": "Welcome to Alltoys!"})


def get_toys(request):
    toys = Toy.objects.all()
    return render(request, "toys/toys.html", context={"toys": toys})
