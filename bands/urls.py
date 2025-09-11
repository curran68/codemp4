from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),  # Homepage
    path('concerts/', views.concert_list, name='concert_list'),
    path('concerts/book_tickets/<int:pk>/', views.book_tickets, name='book_tickets'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='band_list'), name='logout'),  # ✅ redirect home
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('checkout/success/', views.payment_success, name='payment_success'),
    path('checkout/cancel/', views.payment_cancel, name='payment_cancel'),

    # Bands
    path('<slug:slug>/', views.band_detail, name='band_detail'),
]
