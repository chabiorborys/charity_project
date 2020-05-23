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


class Donation(models.Model):
    quantity = models.IntegerField(default=0)
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
