from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.sign_up, name='login'),
    path('details', views.details, name='details'),
]