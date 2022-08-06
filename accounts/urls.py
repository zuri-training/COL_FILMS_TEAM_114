from django.urls import path,include
from . import views

app_name = "accounts"

urlpatterns = [
    #Default auth urls.
    path('', include('django.contrib.auth.urls')),

    #Register Page
    path('register/', views.register, name='register'),

    path('profile/', views.profile, name='profile'),

    path('profile/favourites/', views.list_favourites, name='list_favourites'),

    path('favourites/<int:movie_id>', views.add_favourite, name='add_favourite'),

]