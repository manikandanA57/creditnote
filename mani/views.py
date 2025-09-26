from django.shortcuts import render, redirect
from .forms import EnquiryForm 
from .serializers import EnquirySerializer  

# Web form view
def new_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_success')
    else:
        form = EnquiryForm()
    return render(request, 'mani/new_enquiry.html', {'form': form})

# Home redirect
def home(request):
    return redirect('new_enquiry')

# Success page
def enquiry_success(request):
    return render(request, 'mani/enquiry_success.html')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer

class EnquiryAPI(APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Enquiry created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response(serializer.data)
