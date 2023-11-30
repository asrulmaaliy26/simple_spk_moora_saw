from django.urls import path

from . import views

urlpatterns = [
    path('dataJenisUsaha/', views.dataJenisUsaha, name='dataJenisUsaha'),
    path('dataKuliner/', views.dataKuliner, name='dataKuliner'),
    path('dataKriteria/', views.dataKriteria, name='dataKriteria'),
    path('dataBobot/', views.dataBobot, name='dataBobot'),
    path('dataKonversiPenilaian/', views.dataKonversiPenilaian, name='dataKonversiPenilaian'),
]
 