from django.urls import path
from course import views


urlpatterns = [
    path('course/', views.CourseAPI.as_view()),
]
