from django.contrib import admin
from django.urls import path, include
from rockaria import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),          # Root URL
    path('alt/', views.home, name='home_alt'),
    path('accounts/', include('allauth.urls')),  # Optional alternate URL
    path('bands/', include('bands.urls')),
    path('privacy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms/', views.terms_view, name='terms_of_service'),
    path('contact/', views.contact_view, name='contact'),
]