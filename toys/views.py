from django.shortcuts import render


def dashboard(request):
    return render(request, "toys/dashboard.html", context={"welcome_text": "Welcome to Alltoys!"})
