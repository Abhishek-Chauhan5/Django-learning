from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def blog(request):
    student_list=[
        {"name":"Abhishek", "class":"10th"},
        {"name":"kunal", "class":"11th"},
        {"name":"karan", "class":"12th"},
    ]
    return render(request, 'blog/blog.html',{'students':student_list})
