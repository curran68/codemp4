from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Admin URL is kept here.
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    
    # This correctly sets the root URL to the home page.
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # This includes the URLs from the 'bands' app under the 'bands/' prefix.
    path('bands/', include('bands.urls')),
    
    
    # Standard static pages.
    path('privacy_policy/', TemplateView.as_view(template_name='bands/privacy_policy.html'), name='privacy_policy'),
    path('terms-of-service/', TemplateView.as_view(template_name='bands/terms_of_service.html'), name='terms_of_service'),
    path('contact/', TemplateView.as_view(template_name='bands/contact.html'), name='contact'),
]

# This is for serving static and media files during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)