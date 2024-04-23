from django.contrib import admin
from .models import Organization, Household, Person


class PersonInline(admin.TabularInline):
    model = Person
    extra = 1

class OrgMembersInline(admin.TabularInline):
    model = Organization.member_households.through

class HouseholdInline(admin.TabularInline):
    model = Household
    extra = 1


class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('household_ID', 'household_name')
    inlines = [PersonInline]


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_ID', 'organization_name')
    inlines = [OrgMembersInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_ID', 'get_full_name', 'is_married')


# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Household, HouseholdAdmin)
admin.site.register(Person, PersonAdmin)
