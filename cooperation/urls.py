from django.urls import include, path
from cooperation.views import (CreateJobOpportunityView,JobOpportunityListView,
                                JobOpportunityListViewSuperUser, JobOpportunityDeleteView,
                                CreateApplicationView, ApplicationListView, CreateDelegationRequestView,
                                DelegationRequestListView, CreateRepairManRequestView, RepairManRequestListView,
                                RepairManRequestDeleteView, DelegationRequestDeleteView, ApplicationDeleteView,
                                RepairManRequestCheckView, DelegationRequestCheckView, ApplicationCheckView)

app_name ='cooperation'
urlpatterns = [
    path('create-job-opportunity/',CreateJobOpportunityView, name = 'createjobopportunity'),
    path('job-opportunity-list/',JobOpportunityListView, name = 'jobopportunitylist'),
    path('job-opportunity-list-superuser/',JobOpportunityListViewSuperUser , name = 'jobopportunitylistsuperuser'),
    path('job-opportunity-delete/<int:pk>/',JobOpportunityDeleteView , name = 'jobopportunitydelete'),
    path('apply/<int:pk>/',CreateApplicationView , name = 'createapplicatoin'),
    path('create-delegation-request/',CreateDelegationRequestView , name = 'createdelegationrequest'),
    path('applications-list/',ApplicationListView , name = 'applicationlist'),
    path('delegation-request-list/',DelegationRequestListView , name = 'delegationrequestlist'),
    path('create-repairman-request/',CreateRepairManRequestView , name = 'createrepairmanrequest'),
    path('repairman-request-list/',RepairManRequestListView , name = 'repairmanrequestlist'),
    path('repairman-request-delete/<int:pk>/',RepairManRequestDeleteView , name = 'repairmanrequestdelete'),
    path('delegation-request-delete/<int:pk>/',DelegationRequestDeleteView , name = 'delegationrequestdelete'),
    path('application-delete/<int:pk>/',ApplicationDeleteView , name = 'applicationdelete'),

    path('application-check/<int:pk>/',ApplicationCheckView , name = 'applicationcheck'),
    path('delegation-request-check/<int:pk>/',DelegationRequestCheckView , name = 'delegationrequestcheck'),
    path('repairman-request-check/<int:pk>/',RepairManRequestCheckView , name = 'repairmanrequestcheck'),

]
