from django.shortcuts import render
from django.views import View

from .forms import CharityForm
from .models import Donation, Institution, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
class LandingPageView(View):
    def get(self, request):
        sum_of_all_bags = Donation.sum_of_all_bags()
        sum_of_all_institutions = Institution.sum_of_all_institutions()
        foundations = Institution.all_foundations()
        nonprofits = Institution.all_nonprofits()
        lokals = Institution.all_lokal()
        context = {'sum_of_all_bags': sum_of_all_bags,
                   'sum_of_all_institutions':sum_of_all_institutions,
                   'foundations':foundations,
                   'nonprofits': nonprofits,
                   'lokals':lokals,
                   }
        return render(request, 'index.html', context)

class AddDonationView(View):
    def get(self, request):
        form = CharityForm()
        all_institutions = Institution.objects.all()
        all_categories = Category.objects.all()
        context = {'all_institutions':all_institutions,
                   'all_categories': all_categories,
                   'form':form
                   }
        return render(request, 'form.html', context)

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')









