from django.contrib import admin
from .models import Invoice, CreditNote  # உங்கள் models

admin.site.register(Invoice)
admin.site.register(CreditNote)


# Register your models here.
