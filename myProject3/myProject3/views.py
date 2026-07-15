from django.shortcuts import render

def home(request):
    context = {
        "data" :{"name": "Shiv",
        "age":"Infinite"}
    }
    return render(request, 'index.html', context)