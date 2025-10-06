from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def privacy_policy_view(request):
    return render(request, 'home/privacy.html')


def terms_view(request):
    return render(request, 'home/terms.html')


def contact_view(request):
    return render(request, 'home/contact.html')
