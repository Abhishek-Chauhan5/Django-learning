from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('article/<int:year>/<str:month>/', views.for_years, name='article_by_years'),
    path('article/<int:year>/<str:month>/<int:date>/', views.details, name='details'),
]
