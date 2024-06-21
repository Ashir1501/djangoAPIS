from django.urls import path
from . import views
urlpatterns = [
    path('greet/<str:name>',views.Greetings.as_view(),name='greet'),
    path('validate/',views.ValidateAPI.as_view(),name='validateAPI'),
    path('jokes/',views.JokesAPI.as_view(),name='jokesAPI'),
]