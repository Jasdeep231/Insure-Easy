from django.contrib import admin
from .models import Policy
from .models import PurchasedPolicy

# Register the Policy model to the admin panel
admin.site.register(Policy)
admin.site.register(PurchasedPolicy)
