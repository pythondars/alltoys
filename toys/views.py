from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from toys.models import Toy


class DashboardView(TemplateView):
    template_name = "toys/dashboard.html"
    extra_context = {"welcome_text": "Welcome to Alltoys!"}


class ToysListView(ListView):
    model = Toy
    template_name = "toys/toys.html"
    queryset = Toy.objects.filter()

    def get_queryset(self):
        toys = Toy.objects.filter(created_at__year=timezone.now().year)
        toys = toys.select_related("user")
        toys = toys.prefetch_related("tags")

        return toys


class ToyDetailView(DetailView):
    model = Toy
    template_name = "toys/toy_detail.html"


class ToyCreateView(CreateView):
    model = Toy
    fields = ["name", "description", "price"]
