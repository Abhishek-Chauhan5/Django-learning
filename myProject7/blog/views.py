from django.shortcuts import render
from datetime import datetime

# Create your views here.
def list(request):
    blogs =[
        {"title":"Django Basics","is_featured":True,"author":"Abhishek Singh"},
        {"title":"Django Advanced","is_featured":False,"author":""},
        {"title":"Django rest framework","is_featured":False,"author":"kunal Singh"},
    ]
    context = {
        "blogs": "blogs",
        "today": datetime.now(),
        "html_code":"<h1>Welcome tp my blog</h1>",
    }
    return render(request, 'blog/blog_list.html', context)