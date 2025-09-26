from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone','enquiry_date', 'message']