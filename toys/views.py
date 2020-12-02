from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, UpdateView

from toys.forms import ToyForm
from toys.models import Toy


class DashboardView(TemplateView):
    template_name = "toys/dashboard.html"
    extra_context = {"welcome_text": "Welcome to Alltoys!"}


def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    toys = toys.select_related("user")
    toys = toys.prefetch_related("tags")

    return render(request, "toys/toys.html", context={"toys": toys})


def get_toy_detail(request, **kwargs):
    try:
        toy = Toy.objects.get(pk=kwargs.get("id"))
    except Toy.DoesNotExist:
        return redirect("toys:toys")
    return render(request, "toys/toy_detail.html", context={"toy": toy})

