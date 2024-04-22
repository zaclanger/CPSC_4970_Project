from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('household/<int:household_id>/', views.house_detail, name='household_detail'),
    path('organization/<int:organization_id>/', views.organization_detail, name='organization_detail')
]
