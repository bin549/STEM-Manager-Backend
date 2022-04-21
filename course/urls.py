from django.urls import path
from course import views


urlpatterns = [
    path('course/', views.CourseAPI.as_view()),
    path('course/<str:pk>/', views.CourseAPI.as_view()),
]
