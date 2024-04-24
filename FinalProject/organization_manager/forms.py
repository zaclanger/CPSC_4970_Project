from django import forms
from .models import Person, Household, Organization


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'spouse', 'house']


class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['household_name', 'household_contact', 'members', 'address']

    pass


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

    pass
