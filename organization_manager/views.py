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

    if request.method == 'GET':
        if 'search' in request.GET:
            query = request.GET.get('search')
            print(query)
            household_list = Household.objects.all().filter(pk=query)

            if len(household_list) == 0:
                context['error'] = 'Household not found'
            elif len(household_list) > 1:
                context['error'] = 'Too many households match'
            else:
                household_ID = household_list[0].household_ID
                return HttpResponseRedirect(f'/organization_manager/people/filter/{household_ID}/')

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

def people_in_household(request, household_ID):
    context = {}
    form = HouseholdForm()
    household_list = Household.objects.all().filter(pk=household_ID)
    if len(household_list) == 0:
        return HttpResponseRedirect('/organization_manager/people')
    household = household_list[0]
    person_list = Person.objects.filter(household__in=household_list)
    person_excluded_list = Person.objects.exclude(household__in=household_list)
    context['people'] = person_list
    context['people_ex'] = person_excluded_list
    context['title'] = 'People By Household'
    context['household'] = household

    if request.method == 'POST':
        if 'add' in request.POST:
            pid = request.POST.get('add')
            person = Person.objects.get(pk=pid)
            household.members.add(person)
            household.save()
        elif 'remove' in request.POST:
            pid = request.POST.get('remove')
            person = Person.objects.get(pk=pid)
            household.members.remove(person)
            household.save()
        elif 'edit' in request.POST:
            pid = request.POST.get('edit')
    context['form'] = form
    return render(request, "organization_manager/house-people.html", context)

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

    if request.method == 'GET':
        if 'search' in request.GET:
            query = request.GET.get('search')
            print(query)
            organization_list = Organization.objects.all().filter(pk=query)

            if len(organization_list) == 0:
                context['error'] = 'Organization not found'
            elif len(organization_list) > 1:
                context['error'] = 'Too many organizations match'
            else:
                organization_ID = organization_list[0].org_ID
                return HttpResponseRedirect(f'/organization_manager/households/filter/{organization_ID}/')

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

def households_in_org(request, org_ID):
    context = {}
    form = HouseholdForm()
    organization_list = Organization.objects.all().filter(pk=org_ID)
    if len(organization_list) == 0:
        return HttpResponseRedirect('/organization_manager/households')
    organization = organization_list[0]
    context['title'] = f'Households By Organization'
    context['organization'] = organization

    if request.method == 'POST':
        if 'add' in request.POST:
            hid = request.POST.get('add')
            household = Household.objects.get(pk=hid)
            organization.member_households.add(household)
            organization.save()
        elif 'remove' in request.POST:
            hid = request.POST.get('remove')
            household = Household.objects.get(pk=hid)
            organization.member_households.remove(household)
            organization.save()
        elif 'edit' in request.POST:
            hid = request.POST.get('edit')
    household_list = Household.objects.filter(organization__in=organization_list)
    if len(household_list) == 0:
        return HttpResponseRedirect('/organization_manager/households')
    household_excluded_list = Household.objects.exclude(organization__in=organization_list)
    context['households'] = household_list
    context['households_ex'] = household_excluded_list
    context['form'] = form
    return render(request, "organization_manager/org-households.html", context)

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

def organizations(request):
    context = {}
    form = OrganizationForm()
    organization_list = Organization.objects.all()
    context['organizations'] = organization_list
    context['title'] = 'Organization Database'

    if request.method == 'POST':
        if 'save' in request.POST:
            form = OrganizationForm(request.POST)
            form.save()
            form = OrganizationForm()
        elif 'delete' in request.POST:
            oid = request.POST.get('delete')
            selected_organization = Organization.objects.get(org_ID=oid)
            selected_organization.delete()
        elif 'edit' in request.POST:
            oid = request.POST.get('edit')
    context['form'] = form
    return render(request, "organization_manager/organizations.html", context)


def organization_form(request, org_ID):
    context = {}

    context['title'] = 'Edit Organization'
    context['organization_ID'] = org_ID
    context['households'] = Household.objects.all()
    context['organizations'] = Organization.objects.all()

    if request.method == 'GET':
        if org_ID == 0:
            form = OrganizationForm()
        else:
            organization = Organization.objects.get(pk=org_ID)
            context['organization'] = organization
            form = OrganizationForm(instance=organization)
            context['form'] = form
            return render(request, 'organization_manager/organization.html', context)
    elif request.method == 'POST':
        organization = Organization.objects.get(pk=org_ID)
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/organization_manager/organizations')

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
