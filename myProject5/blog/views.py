from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self,name,age):
        self.name = name
        self.age =age
        
def home(request):
    context = {
        "name": "Mohit Kumar",
        "age": 25,
        "skill":["python", "django", "React"],
        "user":User("kunal", 30),
        "blog":{
            "title": "django template intro",
            "author":{
            "name": "Abhishek Singh",
            },
            "content":"<b>this is bold text</b>",
            "created_at": datetime(2026,7,16,15,1),  # year,month,date,hours,min
        },
        "empty_value": None,
    }
    return render(request, "blog/home.html", context)            