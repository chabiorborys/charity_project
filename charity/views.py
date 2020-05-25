from django.shortcuts import render
from django.views import View
from .models import Donation, Institution

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
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')




def organization_view(request, id):
    institutions = Institution.objects.get(id=id)
    context = {'institution':institutions}
    return render(request, 'index.html', context)