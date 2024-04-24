from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Person, Organization, Household
from .forms import PersonForm, HouseholdForm, OrganizationForm


# Create your views here.

def people(request):
    context = {}
    form = PersonForm()
    person_list = Person.objects.all()
    context['people'] = person_list
    context['title'] = 'People Database'

    if request.method == 'POST':
        if 'save' in request.POST:
            form = PersonForm(request.POST)
            form.save()
            form = PersonForm()
        elif 'delete' in request.POST:
            pid = request.POST.get('delete')
            person = Person.objects.get(person_ID=pid)
            person.delete()
        elif 'edit' in request.POST:
            pid = request.POST.get('edit')
    context['form'] = form
    return render(request, "organization_manager/people.html", context)


def person_form(request, person_ID=0):
    context = {}

    context['title'] = 'Edit Person'
    context['person_ID'] = person_ID
    context['people'] = Person.objects.all()
    context['households'] = Household.objects.all()

    if request.method == 'GET':
        if person_ID == 0:
            form = PersonForm()
        else:
            person = Person.objects.get(pk=person_ID)
            context['person'] = person
            form = PersonForm(instance=person)
            context['form'] = form
            return render(request, 'organization_manager/person.html', context)
    elif request.method == 'POST':
        person = Person.objects.get(pk=person_ID)
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/organization_manager/people')

def households(request):
    context = {}
    form = HouseholdForm()
    household_list = Household.objects.all()
    context['households'] = household_list
    context['title'] = 'Household Database'

    if request.method == 'POST':
        if 'save' in request.POST:
            form = HouseholdForm(request.POST)
            form.save()
            form = HouseholdForm()
        elif 'delete' in request.POST:
            hid = request.POST.get('delete')
            person = Household.objects.get(household_ID=hid)
            person.delete()
        elif 'edit' in request.POST:
            hid = request.POST.get('edit')
    context['form'] = form
    return render(request, "organization_manager/households.html", context)


def household_form(request, household_ID):
    context = {}

    context['title'] = 'Edit Household'
    context['household_ID'] = household_ID
    context['households'] = Household.objects.all()
    context['organizations'] = Organization.objects.all()

    if request.method == 'GET':
        if household_ID == 0:
            form = HouseholdForm()
        else:
            household = Household.objects.get(pk=household_ID)
            context['household'] = household
            form = HouseholdForm(instance=household)
            context['form'] = form
            return render(request, 'organization_manager/household.html', context)
    elif request.method == 'POST':
        household = Household.objects.get(pk=household_ID)
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/organization_manager/households')


def organization_form(request, org_ID):
    form = OrganizationForm()
    organization = Organization.objects.get(pk=org_ID)
    return render(request, "organization_manager/organization.html", {"form": form})

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
