from django.urls import path
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),              # /bands/
    path('concerts/', views.concert_list, name='concert_list'),  # /bands/concerts/
    path('<slug:slug>/', views.band_detail, name='band_detail'), # /bands/some-band-slug/
]
