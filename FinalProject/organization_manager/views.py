from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Person, Organization, Household


# Create your views here.

def person_form(request, person_ID):
    person = Person.objects.get(pk=person_ID)
    return render(request, "organization_manager/person.html", {"person": person})


def household_form(request, household_ID):
    household = Household.objects.get(pk=household_ID)
    return render(request, "organization_manager/household.html", {"household_ID": household_ID})


def organization_form(request, org_ID):
    organization = Organization.objects.get(pk=org_ID)
    return render(request, "organization_manager/organization.html", {"org_ID": org_ID})

class IndexView(generic.ListView):
    template_name = 'organization_manager/index.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'organization_manager/person.html'


class HouseholdDetailView(generic.DetailView):
    model = Household
    template_name = 'organization_manager/household.html'


class OrganizationDetailView(generic.DetailView):
    model = Organization
    template_name = 'organization_manager/organization.html'
