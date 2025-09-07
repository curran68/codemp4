from django.contrib import admin
from django.urls import path, include
from rockaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('bands/', include('bands.urls')),
    path('privacy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms/', views.terms_view, name='terms_of_service'),
    path('contact/', views.contact_view, name='contact'),
]