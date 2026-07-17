from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    post = {
        "title": "my second template post",
        "descriptions":"dajango  is  a high-level python web framework",
        "author": None,
        "created_at": datetime(2026,7,16,17,15),
        "comments_count": 5,
        "tags": ["django", "python","web development"],
        "price":100,
        "number":7,
        
    }
    return render(request,'blog/blog_details.html',{"post":post})
