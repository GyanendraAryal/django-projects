from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path("add/", views.student_create, name="student_create"),
    path("", views.student_list, name="student_list"),
    path("details/<int:id>/", views.student_detail, name="student_detail"),
]
