from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('penilaian/', views.penilaian, name='penilaian'),
    path('normalisasi/', views.normalisasi, name='normalisasi'),
    path('perangkingan/', views.perangkingan, name='perangkingan'),
    path('keputusan/', views.keputusan, name='keputusan'),
]
