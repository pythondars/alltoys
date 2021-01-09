from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render, resolve_url
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from toys.forms.toy import ToyModelForm
from toys.forms.user import LoginForm
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


class ToyCreateView(View):
    template_name = "toys/toy.html"

    def get(self, request):
        if not request.user.is_authenticated:
            url = resolve_url("toys:login") + "?next=" + request.get_full_path()
            return redirect(url)

        form = ToyModelForm()
        return render(request, self.template_name, context={
            "form": form,
        })

    def post(self, request):
        form = ToyModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            toy = form.save()
            return redirect(to="toys:toy_detail", pk=toy.id)

        context = {"form": form}
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = "toys/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("toys:dashboard")

        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            redirect_to = request.GET.get("next")
            if not redirect_to:
                redirect_to = "toys:dashboard"
            return redirect(to=redirect_to)

        context = {"form": form}
        return render(request, self.template_name, context)


class SignOutView(LogoutView):
    pass
