from django.urls import path
from toys import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('toys/', views.get_toys, name="toys"),
]
