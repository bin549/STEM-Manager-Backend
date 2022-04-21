from django.urls import path
from users import views


urlpatterns = [
    path('message/', views.MessageAPI.as_view()),
    path('message/<str:pk>/', views.MessageAPI.as_view()),
]
