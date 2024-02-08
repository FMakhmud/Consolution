from django.shortcuts import render
from .models import Banner, Static, Contact


# Create your views here.
def home(request):
    banners = Banner.objects.all()
    statics = Static.objects.all()
    contacts = Contact.objects.all()

    context = {"banners": banners, "statics": statics, "contacts": contacts}
    return render(request, template_name='index.html', context=context)
