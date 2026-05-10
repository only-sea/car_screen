from django.urls import path
from myApp import views

urlpatterns = [
    path('center/', views.center, name='center'),
    path('centerleft/', views.centerleft, name='centerleft'),
    path('bottomleft/', views.bottomleft, name='bottomleft'),
    path('centerright/', views.centerright, name='centerright'),
    path('centermostright/<int:energyType>/', views.centermostright, name='centermostright'),
    path('bottomright/', views.bottomright, name='bottomright'),
]
