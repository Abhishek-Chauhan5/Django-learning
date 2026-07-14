from django.http import HttpResponse

# Create your views here.

def post_details(request, post_id):
    return HttpResponse(f"<h1>Show Blog Post {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Profile of User: {username}</h1>")

def article_by_years(request, year):
    return HttpResponse(f"<h1> article of the year is: {year}</h1>")

def for_years(request, year, month):
    return HttpResponse(f"<h1>new time is: {year} - {month}</h1>")

def details(request, **kwargs):
    return HttpResponse(f"<h1>Data: {kwargs}</h1>")