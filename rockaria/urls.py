from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from bands.views import contact_view  # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('bands/', include('bands.urls')),
    
    # Updated contact URL to use the view
    path('contact/', contact_view, name='contact'),
    
    # Other static pages
    path('privacy_policy/', TemplateView.as_view(template_name='bands/privacy_policy.html'), name='privacy_policy'),
    path('terms-of-service/', TemplateView.as_view(template_name='bands/terms_of_service.html'), name='terms_of_service'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)