from django.shortcuts import render


# Create your views here.
def hii(request):
    cont = {
        "name": "kunal",
    }
    return render(request, 'blog/blog.html' , {"cont":cont})