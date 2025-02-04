from django.test import TestCase
from ..models import *
from django.contrib.auth.models import User
 
class PolicyModelTest(TestCase):
    def test_policy_creation(self):
        policy=Policy.objects.create(name="Health Insurance",
                                     description="Cover medical Expense",
                                     premium=5000,
                                     duration_years=5)
        self.assertEqual(policy.name,"Health Insurance")
        self.assertEqual(policy.description,"Cover medical Expense")
        self.assertEqual(policy.premium,5000)
        self.assertEqual(policy.duration_years,5)
 
class PurchasedPolicyTest(TestCase):
    def test_purchase_policy(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.policy=Policy.objects.create(name="Car Insurance",
                                     description="Cover car damage expense",
                                     premium=5000,
                                     duration_years=5)
        self.purchased_policy=PurchasedPolicy.objects.create(
            user=self.user,
            policy=self.policy
        )
 
        self.assertEqual(self.purchased_policy.user.username, "testuser")
        self.assertEqual(self.purchased_policy.policy.name, "Car Insurance")
        self.assertIsNotNone(self.purchased_policy.purchase_date)