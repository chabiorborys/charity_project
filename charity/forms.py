from django import forms

from charity.models import Category, Institution


class CharityForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    number_of_items = forms.IntegerField()
    organization = forms.ModelChoiceField(queryset=Institution.objects.all())