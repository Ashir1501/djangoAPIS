from django.urls import path
from . import views
urlpatterns = [
    path('api/greet/',views.Greetings.as_view(),name='greet'),
    path('api/validate/',views.ValidateAPI.as_view(),name='validateAPI'),
    path('api/jokes/',views.JokesAPI.as_view(),name='jokesAPI'),
    path('',views.Dashboard.as_view(),name='home'),
]