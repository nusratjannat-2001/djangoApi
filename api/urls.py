from django.urls import path
from . import views


urlpatterns = (

    path("breeds/", views.BreedList.as_view(), name="breedList"),
    path("breeds/<int:pk>", views.BreedDeletePut.as_view(), name="breed-delete-put"),
    path("dogs/", views.DogList.as_view(), name="dogList"),
    path("dogs/<int:pk>", views.DogDeletePut.as_view(), name="dog-delete-put"),

)
