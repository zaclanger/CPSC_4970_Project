from django.db import models

# Create your models here.


class Organization(models.Model):
    org_ID = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=80, null=False)
    organization_description = models.TextField(null=True, blank=True)
    member_households = models.ManyToManyField('Household', blank=True)

    def __str__(self):
        return self.organization_name

    def get_info(self):
        return f"""
                Organization: {self.org_ID}
                Name: {self.organization_name}
                Description: {self.organization_description}
                """


class Household(models.Model):
    household_ID = models.AutoField(primary_key=True)
    household_name = models.CharField(max_length=20, default='household_ID', null=False)
    household_contact = models.ForeignKey('Person', related_name='contact_person', on_delete=models.SET_NULL,
                                          null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.household_ID)

    def get_info(self):
        return f"""
                Household ID: {self.household_ID}
                Organizations: {[org.organization_name for org in self.organization_set]}
                Household Contact: {self.household_contact}
                Address: {self.address}
                """


class Person(models.Model):
    person_ID = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=20, default="", null=True, blank=True)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=True, blank=True)
    spouse = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.get_full_name()}"

    def get_info(self):
        out = f"""
                Person ID: {self.person_ID}
                Household: {self.household}
                Name: {self.get_full_name()}
                Email: {self.email}
                """
        if self.is_married():
            out += f"Spouse: {self.spouse}"

        return out

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def is_married(self):
        return self.spouse is not None
