from django.shortcuts import render
from django.views import View
from .models import Donation, Institution

class LandingPageView(View):
    def get(self, request):
        sum_of_all_bags = Donation.sum_of_all_bags()
        sum_of_all_institutions = Institution.sum_of_all_institutions()
        context = {'sum_of_all_bags': sum_of_all_bags,
                   'sum_of_all_institutions':sum_of_all_institutions
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


class OrganizationCountView(View):
    def get(self, request):
        obj = Institution.objects.all().count()
        context = {'number_of_institutions': obj.name}
        return render(request, 'index.html', context)


def organization_view(request, id):
    institutions = Institution.objects.get(id=id)
    context = {'institution':institutions}
    return render(request, 'index.html', context)