from django.test import TestCase
from .models import *
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

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

class PolicyViewTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.user=User.objects.create_user(username="testuser",password="12345")
        self.policy=Policy.objects.create(name='Test Policy', description='Test Description', premium=100, duration_years=1)
        self.client.login(username="testuser",password="12345")

    def test_policy_list_view(self):
        response=self.client.get(reverse('policy_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'insurance/policy_list.html')
        self.assertContains(response,self.policy.name)

    def test_purchase_policy_view(self):
        response = self.client.post(f'/purchase/{self.policy.id}/')
        self.assertEqual(response.status_code, 302)  # Redirect to 'my_policies'
        self.assertEqual(PurchasedPolicy.objects.filter(user=self.user, policy=self.policy).count(),1)

    def test_purchase_existing_policy(self):
        PurchasedPolicy.objects.create(user=self.user,policy=self.policy)
        response=self.client.get(f'/purchase/{self.policy.id}/')
        # response = self.client.get(reverse('purchase_policy', args=[self.policy.id]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'insurance/choose_policy.html')

    def test_my_policies_view(self):
        PurchasedPolicy.objects.create(user=self.user, policy=self.policy)
        # response = self.client.get(reverse('my_policies'))
        response = self.client.get('/my-policies/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'insurance/my_policies.html')
        self.assertContains(response, self.policy.name)