from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('signin', views.signin, name='signin'),
    path('registration', views.registration, name='registration')
]