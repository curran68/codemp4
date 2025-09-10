from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),              # /bands/
    path('concerts/', views.concert_list, name='concert_list'),  # /bands/concerts/
    path('concerts/book_tickets/<int:pk>/', views.book_tickets_for_concert, name='book_tickets_for_concert'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('accounts/', include('allauth.urls')),  # This handles login, logout, register etc.
    path('profile/', views.profile_view, name='profile'),
    path('<slug:slug>/', views.band_detail, name='band_detail'), # This should be last
]