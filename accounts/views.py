
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from movies.forms import CustomUserCreationForm, UserInfoForm
from django.contrib.auth.models import User
from movies.models import Movie

# def register(request):
#     """Register a new user"""
#     if request.method != 'POST':
#         #Display blank form
#         form = CustomUserCreationForm()
#     else:
#         # Process the completed form
#         form = CustomUserCreationForm(data=request.POST)

#         if form.is_valid:
#             new_user = form.save()

#             #Login the user in and redirect to home page

#             login(request, new_user)
#             return redirect('movies:index')

#     # Display Form filled or invalid
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)
from django.http import HttpResponse


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank form
        form = CustomUserCreationForm()
        user_info_form = UserInfoForm()
    else:
        # Process the completed form
        form = CustomUserCreationForm(data=request.POST)
        user_info_form = UserInfoForm(request.POST, request.FILES or None)


        if form.is_valid and user_info_form.is_valid():
            new_user = form.save()

            profile = user_info_form.save(commit=False)
            profile.user = new_user
            profile.save()            


            login(request,new_user)
            return redirect('movies:index')
        else:
            return redirect('accounts:register')

    # Display Form filled or invalid
    context = {'form': form, 'user_info_form': user_info_form}
    return render(request, 'registration/register.html', context)


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from movies.models import Movie, MovieComment
from django.http import Http404 

@login_required
def add_favourite(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie.favourites.filter(id=request.user.id).exists():
        movie.favourites.remove(request.user)
    else:
        movie.favourites.add(request.user)
    return redirect('movies:view_movie', movie_id = movie_id)


@login_required
def list_favourites(request):
    favourites = Movie.objects.filter(favourites=request.user)

    context = {'favourites' : favourites}

    return render(request, 'favourites.html', context)

@login_required
def profile(request):
    user = request.user 

    movies = Movie.objects.filter(author=request.user)

    favourites = Movie.objects.filter(favourites=request.user)

    context = {'favourites' : favourites, 'movies' : movies, 'user' : user}

    return render(request, 'profile.html', context)
