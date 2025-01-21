from django.db import models

# Create your models here.
# insurance/models.py

from django.db import models
from django.contrib.auth.models import User

class Policy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    duration_years = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class PurchasedPolicy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchased_policies')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.policy.name}"
