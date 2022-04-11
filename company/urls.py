from django.urls import include, path
from company.views import (ContactUsView, AboutUsView, ContactUsListView,
                            ContactUsDeleteView, ComplaintView, ComplaintDeleteView,
                            ComplaintListView, CreateFeedbackView, FeedbackListView,
                            FeedbackDeleteView)

app_name ='company'
urlpatterns = [
    path('about-us/',AboutUsView, name = 'about-us'),
    path('contact-us/',ContactUsView, name = 'contact-us'),
    path('create-feedback/',CreateFeedbackView, name = 'createfeedback'),
    path('feedback-list/',FeedbackListView, name = 'feedbacklist'),
    path('complaint/',ComplaintView, name = 'complaint'),
    path('contact-us-list/',ContactUsListView, name = 'contact-us-list'),
    path('complaint-list/',ComplaintListView, name = 'complaint-list'),
    path('contact-us-delete/<int:pk>/',ContactUsDeleteView, name = 'contact-us-delete'),
    path('feedback-delete/<int:pk>/',FeedbackDeleteView, name = 'feedback-delete'),
    path('complaint-delete/<int:pk>/',ComplaintDeleteView, name = 'complaint-delete'),

]
