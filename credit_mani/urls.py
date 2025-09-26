from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CreditNoteViewSet,CustomerViewset,InvoiceViewset

router = DefaultRouter()
router.register(r'credit-notes',CreditNoteViewSet) 
router.register(r'customers',CustomerViewset)
router.register(r'invoices',InvoiceViewset) 

urlpatterns = [
      
    path ('',include(router.urls)),
    
    
    
]