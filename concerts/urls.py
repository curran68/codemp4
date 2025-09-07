from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('concerts/', views.concert_list, name='concert_list'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # your existing home view
    path('concerts/', include('concerts.urls')),  # Add this
]