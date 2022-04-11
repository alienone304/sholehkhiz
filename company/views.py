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

from .models import ContactUsModel, ComplaintModel, FeedbackModel
from .forms import ContactUsForm, ComplaintForm, FeedbackForm
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

             if 'rate_cleanness' in request.POST:
                 complaint.rate_cleanness = request.POST['rate_cleanness']

             if 'rate_beautiness' in request.POST:
                 complaint.rate_beautiness = request.POST['rate_beautiness']

             if 'rate_clothes' in request.POST:
                 complaint.rate_clothes = request.POST['rate_clothes']

             if 'rate_behaviour' in request.POST:
                 complaint.rate_behaviour = request.POST['rate_behaviour']

             if 'rate_effectiveness' in request.POST:
                 complaint.rate_effectiveness = request.POST['rate_effectiveness']

             if 'rate_overall' in request.POST:
                 complaint.rate_overall = request.POST['rate_overall']

             if 'visiting_day' in request.POST:
                 complaint.visiting_day = request.POST['visiting_day']
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


def CreateFeedbackView(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(data = request.POST)
        if feedback_form.is_valid():
             feedback = feedback_form.save(commit=False)
             if 'does_visit_on_time' in request.POST:
                 feedback.does_visit_on_time = request.POST['does_visit_on_time']

             if 'does_have_card' in request.POST:
                 feedback.does_have_card = request.POST['does_have_card']

             if 'does_gave_tutorial' in request.POST:
                 feedback.does_gave_tutorial = request.POST['does_gave_tutorial']

             if 'does_solve_problem' in request.POST:
                 feedback.does_solve_problem = request.POST['does_solve_problem']

             if 'does_give_factor' in request.POST:
                 feedback.does_give_factor = request.POST['does_give_factor']

             if 'does_announce_cost' in request.POST:
                 feedback.does_announce_cost = request.POST['does_announce_cost']

             if 'does_gave_label' in request.POST:
                 feedback.does_gave_label = request.POST['does_gave_label']

             if 'does_satisfy_you' in request.POST:
                 feedback.does_satisfy_you = request.POST['does_satisfy_you']

             if 'number_of_visits' in request.POST:
                 feedback.number_of_visits = request.POST['number_of_visits']
             feedback.save()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(feedback_form.errors)
    else:
        feedback_form = FeedbackForm()
    return render(request,'company/createfeedback.html',
                  {'form':feedback_form})


@login_required
@superuser_required
def FeedbackListView(request):
    feedbacks = FeedbackModel.objects.all()
    return render(request,'company/feedbacklist.html',
                  {'feedbacks':feedbacks})


@login_required
@superuser_required
def FeedbackDeleteView(request):
    feedback = get_object_or_404(FeedbackModel,pk = pk)
    feedback.delete()
    return HttpResponseRedirect(reverse('company:feedbacklist'))
