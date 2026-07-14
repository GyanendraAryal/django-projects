from django.shortcuts import render
from datetime import datetime


# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    context = {
        "name": "Gyanendra Aryal",
        "age": 19,
        "skills": ["python", "django", "React"],
        "user": User("Aryal", 19),
        "blog": {
            "title": "Django Template Intro",
            "content": "<b> This is bold</b>",
            "created_at": datetime(2025, 8, 18, 10, 30),
        },
        "empty_value": None,
    }
    return render(request, "blog/home.html", context)
