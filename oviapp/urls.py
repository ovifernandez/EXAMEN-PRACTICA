from oviapp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('motos/', views.motos, name='motos'),
    path('moto/<int:pk>', views.MotoDetailView.as_view(), name='moto_detail'),
    path('cruise/<int:pk>', views.MarcaDetailView.as_view(), name='marca_detail'),
]
