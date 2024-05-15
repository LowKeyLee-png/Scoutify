from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('search_players/', views.search_players, name='search_players'),
]