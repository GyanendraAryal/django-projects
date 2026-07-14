from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    blogs = [
        {
            "title": "Getting Started with Python",
            "is_featured": True,
            "author": "Alice Johnson",
        },
        {
            "title": "Understanding Django Models",
            "is_featured": False,
            "author": "Bob Smith",
        },
        {
            "title": "REST APIs with FastAPI",
            "is_featured": True,
            "author": "Charlie Brown",
        },
        {
            "title": "Introduction to Docker",
            "is_featured": False,
            "author": "Diana Lee",
        },
        {
            "title": "Deploying Applications with Kubernetes",
            "is_featured": False,
            "author": "Ethan Wilson",
        },
        {
            "title": "Mastering Git and GitHub",
            "is_featured": True,
            "author": "Fiona Carter",
        },
        {
            "title": "Building Responsive Web Apps",
            "is_featured": False,
            "author": "George Miller",
        },
        {
            "title": "A Beginner's Guide to Machine Learning",
            "is_featured": True,
            "author": "Hannah Davis",
        },
        {
            "title": "Effective SQL Query Optimization",
            "is_featured": False,
            "author": "Ian Thompson",
        },
        {
            "title": "Modern JavaScript Best Practices",
            "is_featured": False,
            "author": "Julia Roberts",
        },
    ]
    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "is_featured": True,
        "html_code": "<b>Welcome to My Blog</b>",
    }
    return render(request, "blog/blog_list.html", context)
