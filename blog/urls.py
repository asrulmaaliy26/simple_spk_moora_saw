from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tabeldatabase/', include(('tabeldatabase.urls','tabeldatabase'), namespace='tabeldatabase')),
    path('saw/', include(('saw.urls','saw'), namespace='saw')),
    path('moora/', include(('moora.urls','moora'), namespace='moora')),
]
