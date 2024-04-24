from django.urls import path
from . import views

app_name = 'organization_manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('people/', views.people, name='people'),
    path('person/<int:person_ID>/', views.person_form, name='update_person'),
    path('households/', views.households, name='households'),
    path('household/<int:household_ID>/', views.household_form, name='update_household'),
    path('organization/<int:org_ID>/', views.organization_form, name='update_organization')
]
#    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
#    path('person/<int:person_ID>/', views.person_form, name='update_person'),
#    path('household/<int:pk>/', views.HouseholdDetailView.as_view(), name='household_detail'),
#    path('organization/<int:pk>/', views.OrganizationDetailView.as_view(), name='organization_detail'),
