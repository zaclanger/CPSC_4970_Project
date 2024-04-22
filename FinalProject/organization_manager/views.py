from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person, Organization, Household


# Create your views here.

def index(request):
    person_list = Person.objects.all()
    context = {
        "person_list": person_list,
    }
    return render(request, 'organization_manager/index.html', context)

def person_detail(request, person_id):
    person = Person.objects.get(person_ID=person_id)
    out =   f"""
            Here's the detailed info about person {person.person_ID}:
            {repr(person)}
            """
    return HttpResponse(out)

def organization_detail(request, organization_id):
    organization = Organization.objects.get(organization_ID=organization_id)
    out =   f"""
            Here's the detailed info about organization {organization.organization_ID}:
            {repr(organization)}
            """
    return HttpResponse(out)

def house_detail(request, household_id):
    household = Household.objects.get(household_ID=household_id)
    out =   f"""
            Here's the detailed info about household {household_id}:
            {repr(household)}
            """
    return HttpResponse(repr(household))
