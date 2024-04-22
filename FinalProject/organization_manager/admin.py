from django.contrib import admin
from .models import Organization, Household, Person

# Register your models here.
admin.site.register(Organization)
admin.site.register(Household)
admin.site.register(Person)
