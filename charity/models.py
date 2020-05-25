from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    FOUNDATION = 0
    NONPROFIT = 1
    LOKAL = 2
    FOUNDATIONS = (
        (FOUNDATION, "fundacja"),
        (NONPROFIT, "organizacja pozarządowa"),
        (LOKAL, "zbiórka lokalna")
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=FOUNDATIONS, default=FOUNDATION)
    categories = models.ManyToManyField('Category')

    def sum_of_all_institutions():
        return (Institution.objects.all().count())

    def all_foundations():
        return Institution.objects.all().filter(type=Institution.FOUNDATION)

    def all_nonprofits():
        return Institution.objects.all().filter(type=Institution.NONPROFIT)

    def all_lokal():
        return Institution.objects.all().filter(type=Institution.LOKAL)

    def is_foundation(self):
        return self.type == Institution.FOUNDATION




class Donation(models.Model): #aggregate albo annotate, sum/count naprzemiennie
    quantity = models.IntegerField(default=0)

    def sum_of_all_bags():
        sum = 0
        for d in Donation.objects.all():
            sum += d.quantity
        return sum

    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
