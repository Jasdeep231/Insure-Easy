# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from ..models import *

# class PolicyViewTest(TestCase):
#     def setUp(self):
#         self.client=Client()
#         self.user=User.objects.create_user(username="testuser",password="12345")
#         self.policy=Policy.objects.create(name='Test Policy', description='Test Description', premium=100, duration_years=1)
#         self.client.login(username="testUser",password="12345")

#     def test_policy_list_view(self):
#         response=self.client.get(reverse('policy_list'))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'insurance/policy_list.html')
#         self.assertContains(response,self.policy.name)
        