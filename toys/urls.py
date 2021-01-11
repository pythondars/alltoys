from django.urls import path
from toys import views

app_name = "toys"
urlpatterns = [
    path('', views.ToysListView.as_view(), name="toys"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.SignOutView.as_view(), name="logout"),
    # path('toys/', views.ToysListView.as_view(), name="toys"),
    path('toys/create/', views.ToyCreateView.as_view(), name="toys-create"),
    path('toys/<int:pk>/', views.ToyDetailView.as_view(), name="toy_detail"),
]
