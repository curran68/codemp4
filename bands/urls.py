from django.urls import path
from . import views

urlpatterns = [

    path('concerts/', views.concert_list, name='concert_list'),  # /bands/concerts/
    path('concerts/book_tickets/<int:pk>/', views.book_tickets, name='book_tickets_for_concert'),
    path('<slug:slug>/', views.band_detail, name='band_detail'), # /bands/some-band-slug/
    path('', views.band_list, name='band_list'),              # /bands/
    
]
