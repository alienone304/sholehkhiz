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

from .models import ContactUsModel, ComplaintModel
from .forms import ContactUsForm, ComplaintForm
from accounts.decorators import superuser_required

def AboutUsView(request):

    return render(request,'company/about-us.html')


def ContactUsView(request):
    if request.method == 'POST':
        contactus_form = ContactUsForm(data = request.POST)
        if contactus_form.is_valid():
             contactus = contactus_form.save(commit=False)
             contactus.save()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(contactus_form.errors)
    else:
        contactus_form = ContactUsForm()
    return render(request,'company/contactus.html',
                  {'contactus_form':contactus_form})


def ComplaintView(request):
    if request.method == 'POST':
        complaint_form = ComplaintForm(data = request.POST)
        if complaint_form.is_valid():
             complaint = complaint_form.save(commit=False)
             if 'picture' in request.FILES:
                 complaint.picture = request.FILES['picture']

             complaint.save()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(complaint_form.errors)
    else:
        complaint_form = ComplaintForm()
    return render(request,'company/complaint.html',
                  {'complaint_form':complaint_form})


@login_required
@superuser_required
def ContactUsListView(request):
    try:
        contactus_list = get_list_or_404(ContactUsModel.objects.order_by('contacted_at'))
        return render(request,'company/contactuslist.html',
                      {'contactus_list':contactus_list})
    except:
        return render(request,'company/contactuslist.html')


@login_required
@superuser_required
def ComplaintListView(request):
    try:
        complaint_list = get_list_or_404(ComplaintModel.objects.order_by('complained_at'))
        return render(request,'company/complaintlist.html',
                      {'complaint_list':complaint_list})
    except:

         return render(request,'company/complaintlist.html')


@login_required
@superuser_required
def ContactUsDeleteView(request, pk):
    contactus = get_object_or_404(ContactUsModel, pk = pk)
    contactus.delete()
    return HttpResponseRedirect(reverse('company:contact-us-list'))


@login_required
@superuser_required
def ComplaintDeleteView(request, pk):
    complaint = get_object_or_404(ComplaintModel, pk = pk)
    complaint.delete()
    return HttpResponseRedirect(reverse('company:complaint-list'))
