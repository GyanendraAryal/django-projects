from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    post = {
        "title":"My Second Template post",
        "description":"Django is a high-level python web-framework",
        "author":False,
        "created_at":datetime(2025,8,19,12,30),
        "comments_count":5,
        "tags":["Django","Python","Web Development"],
        "price":100,
        "number":7,
    }
    return render(request, 'blog/blog_details.html',{"post":post})
