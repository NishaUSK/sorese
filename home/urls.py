from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.footer, name='footer'),
    path('', views.header, name='header'),
    path('', views.jumbotron1, name='jumbotron1'),
    path('', views.jumbotron2, name='jumbotron2'),
    path('', views.jumbotron3, name='jumbotron3'),
]
