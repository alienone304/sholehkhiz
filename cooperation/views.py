from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404

#handmade
from cooperation.models import JobOpportunityModel, ApplicationModel, DelegationRequestModel, RepairManRequestModel
from cooperation.forms import JobOpportunityForm, ApplicationForm, DelegationRequestForm, RepairManRequestForm
from accounts.decorators import superuser_required


@login_required
@superuser_required
def CreateJobOpportunityView(request):
    if request.method == 'POST':
        job_opportunity_form = JobOpportunityForm(data = request.POST)
        if job_opportunity_form.is_valid():
             job_opportunity = job_opportunity_form.save(commit=False)
             job_opportunity.save()
             return HttpResponseRedirect(reverse('accounts:superuserdashboard'))
        else:
            print(job_opportunity_form.errors)
    else:
        job_opportunity_form = JobOpportunityForm()
    return render(request,'cooperation/createjobopportunity.html',
                  {'job_opportunity_form':job_opportunity_form})



def JobOpportunityListView(request):
    try:
        job_opportunity_list = get_list_or_404(JobOpportunityModel.objects.all())
        return render(request,'cooperation/jobopportunitylist.html',
                      {'job_opportunity_list':job_opportunity_list})
    except:
        return render(request,'cooperation/jobopportunitylist.html')


@login_required
@superuser_required
def JobOpportunityListViewSuperUser(request):
    try:
        job_opportunity_list = get_list_or_404(JobOpportunityModel.objects.all())
        return render(request,'cooperation/jobopportunitylistsuperuser.html',
                      {'job_opportunity_list':job_opportunity_list})
    except:
        return render(request,'cooperation/jobopportunitylistsuperuser.html')


@login_required
@superuser_required
def JobOpportunityDeleteView(request, pk):
    job_opportunity = get_object_or_404(JobOpportunityModel, pk = pk)
    job_opportunity.delete()
    return HttpResponseRedirect(reverse('cooperation:jobopportunitylistsuperuser'))


def CreateApplicationView(request,pk):
    job = get_object_or_404(JobOpportunityModel, pk= pk)
    if request.method == 'POST':
        application_form = ApplicationForm(data = request.POST)
        if application_form.is_valid():
             application = application_form.save(commit=False)
             application.job = job
             if 'resome' in request.FILES:
                application.resome = request.FILES['resome']
             application.save()
             return HttpResponseRedirect(reverse('cooperation:jobopportunitylist'))
        else:
            print(application_form.errors)
    else:
        application_form = ApplicationForm()
    return render(request,'cooperation/createapplication.html',
                  {'application_form':application_form})


@login_required
@superuser_required
def ApplicationListView(request):
    try:
        application_list = get_list_or_404(ApplicationModel.objects.all().order_by('checked_at'))
        return render(request,'cooperation/applicationlist.html',
                      {'application_list':application_list})
    except:
        return render(request,'cooperation/applicationlist.html')


@login_required
@superuser_required
def ApplicationDeleteView(request, pk):
    application = get_object_or_404(ApplicationModel, pk = pk)
    application.delete()
    return HttpResponseRedirect(reverse('cooperation:applicationlist'))


@login_required
@superuser_required
def ApplicationCheckView(request, pk):
    application = get_object_or_404(ApplicationModel, pk = pk)
    if application.checked_at:
        pass
    else:
        application.checked_at = timezone.now()
    application.save()
    return HttpResponseRedirect(reverse('cooperation:applicationlist'))



def CreateDelegationRequestView(request):
    if request.method == 'POST':
        delegation_request_form = DelegationRequestForm(data = request.POST)
        if delegation_request_form.is_valid():
             delegation_request = delegation_request_form.save(commit=False)
             delegation_request.save()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(delegation_request_form.errors)
    else:
        delegation_request_form = DelegationRequestForm()
    return render(request,'cooperation/createdelegationrequest.html',
                  {'delegation_request_form':delegation_request_form})


@login_required
@superuser_required
def DelegationRequestListView(request):
    try:
        delegation_request_list = get_list_or_404(DelegationRequestModel.objects.all().order_by('checked_at'))
        return render(request,'cooperation/delegationrequestlist.html',
                      {'delegation_request_list':delegation_request_list})
    except:
        return render(request,'cooperation/delegationrequestlist.html')


@login_required
@superuser_required
def DelegationRequestDeleteView(request, pk):
    delegation_request = get_object_or_404(DelegationRequestModel, pk = pk)
    delegation_request.delete()
    return HttpResponseRedirect(reverse('cooperation:delegationrequestlist'))


@login_required
@superuser_required
def DelegationRequestCheckView(request, pk):
    delegation_request = get_object_or_404(DelegationRequestModel, pk = pk)
    if delegation_request.checked_at:
        pass
    else:
        delegation_request.checked_at = timezone.now()
    delegation_request.save()
    return HttpResponseRedirect(reverse('cooperation:delegationrequestlist'))


def CreateRepairManRequestView(request):
    if request.method == 'POST':
        repairman_request_form = RepairManRequestForm(data = request.POST)
        if repairman_request_form.is_valid():
             repairman_request = repairman_request_form.save(commit=False)
             repairman_request.saDeleteve()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(repairman_request_form.errors)
    else:
        repairman_request_form = RepairManRequestForm()
    return render(request,'cooperation/createrepairmanrequest.html',
                  {'repairman_request_form':repairman_request_form})


@login_required
@superuser_required
def RepairManRequestListView(request):
    try:
        repairman_request_list = get_list_or_404(RepairManRequestModel.objects.all().order_by('checked_at'))
        return render(request,'cooperation/repairmanrequestlist.html',
                      {'repairman_request_list':repairman_request_list})
    except:
        return render(request,'cooperation/repairmanrequestlist.html')


@login_required
@superuser_required
def RepairManRequestDeleteView(request, pk):
    repairman_request = get_object_or_404(RepairManRequestModel, pk = pk)
    repairman_request.delete()
    return HttpResponseRedirect(reverse('cooperation:repairmanrequestlist'))


@login_required
@superuser_required
def RepairManRequestCheckView(request, pk):
    repairman_request = get_object_or_404(RepairManRequestModel, pk = pk)
    if repairman_request.checked_at:
        pass
    else:
        repairman_request.checked_at = timezone.now()
    repairman_request.save()
    return HttpResponseRedirect(reverse('cooperation:repairmanrequestlist'))
