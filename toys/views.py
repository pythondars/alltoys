from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render, resolve_url
from django.views import View
from django.views.generic import DetailView

from toys.forms.toy import ToyModelForm
from toys.forms.user import LoginForm
from toys.models import Toy


class ToysListView(View):
    template_name = "toys/toys.html"

    def get(self, request, *args, **kwargs):
        toys = Toy.objects.all()
        return render(request, self.template_name, context={
            "toys": toys,
        })


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
