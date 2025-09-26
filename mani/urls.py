from django.urls import path
from . import views
from .views import EnquiryAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('enquiry/new/', views.new_enquiry, name='new_enquiry'),
    path('enquiry/success/', views.enquiry_success, name='enquiry_success'),
    
    
    path('api/enquiry/', EnquiryAPI.as_view(), name='api_enquiry'),
]
