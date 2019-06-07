from django.shortcuts import render
from .models import Lifestyle, Lifestyle_detail, Portrait, Portrait_detail



def home(request):
    portrait = Portrait.objects.all()[0]
    lifestyle = Lifestyle.objects.all()[0]
    return render(request, 'photo/home.html',{'portrait':portrait, 'lifestyle': lifestyle, 'home_page': 'active'})


def portraitDetail(request):
    portraits = Portrait_detail.objects.all()
    return render(request, 'photo/portraits.html', {'portraits': portraits, 'portrait_page': 'active'})


def lifestyleDetail(request):
    lifestyles = Lifestyle_detail.objects.all()
    return render(request, 'photo/lifestyle.html', {'lifestyles': lifestyles, 'lifestyle_page': 'active'})  

