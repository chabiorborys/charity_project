from django.shortcuts import render, redirect
from django.views import View

from .forms import CharityForm, RegistrationForm
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
                   'sum_of_all_institutions': sum_of_all_institutions,
                   'foundations': foundations,
                   'nonprofits': nonprofits,
                   'lokals': lokals,
                   }
        return render(request, 'index.html', context)


class AddDonationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = CharityForm()
            all_institutions = Institution.objects.all()
            all_categories = Category.objects.all()
            context = {'all_institutions': all_institutions,
                    'all_categories': all_categories,
                    'form': form
                    }
            return render(request, 'form.html', context)
        else:
            return redirect('/login/')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/register")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = password
            form = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                            password=password, username=email)
            form.save()
            return render(request, 'login.html', {'form': form})
        return render(request, 'register.html')
