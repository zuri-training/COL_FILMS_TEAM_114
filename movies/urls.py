"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search_movies, name='search_movies'),
    
    path('new_movie/', views.new_movie, name='new_movie'),
    
    path('movies/', views.all_movies, name='all_movies'),
    
    path('view_movie/<int:movie_id>', views.view_movie, name='view_movie'),

    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),

    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    
    path('view-profile/<int:movie_id>/', views.view_profile, name='view_profile'),

    path('viewcommentprofile/<int:comment_id>/', views.view_comment_profile, name='view_comment_profile'),   

    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),

    path('view_movie/<int:movie_id>/new_comment/', views.new_comment, name='new_comment'),

    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),

]