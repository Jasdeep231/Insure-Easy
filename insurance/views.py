from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from insurance.models import Policy, PurchasedPolicy
from .serializers import PolicySerializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'insurance/policy_list.html', {'policies': policies})

@login_required
def purchase_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    
    # Check if the user already has a purchased policy for this type
    existing_policy = PurchasedPolicy.objects.filter(user=request.user, policy=policy).first()
    if existing_policy:
        # Prompt the user to choose between buying a new policy or continuing with the existing one
        if request.method == 'POST':
            if 'buy_new_policy' in request.POST:
                # Create a new policy
                # existing_policy.expired_on = timezone.now() + timedelta(days=policy.duration_years * 365)
                # existing_policy.purchase_date = timezone.now()
                # existing_policy.save()
                PurchasedPolicy.objects.create(
                    user=request.user, 
                    policy=policy,
                    expired_on=timezone.now() + timedelta(days=policy.duration_years * 365)
                )
                return redirect('my_policies')
            elif 'continue_existing_policy' in request.POST:
                # User chose to continue with the existing policy
                return redirect('my_policies')
        return render(request, 'insurance/choose_policy.html', {'existing_policy': existing_policy, 'policy': policy})

    PurchasedPolicy.objects.create(
        user=request.user, 
        policy=policy,
        expired_on=timezone.now() + timedelta(days=policy.duration_years * 365)
    )
    return redirect('my_policies')

@login_required
def my_policies(request):
    purchased_policies = PurchasedPolicy.objects.filter(user=request.user)
    return render(request, 'insurance/my_policies.html', {'purchased_policies': purchased_policies})


# API
class API(GenericAPIView):
    serializer_class = PolicySerializers

    def get(self, request):
        objects = Policy.objects.all()
        serializer = PolicySerializers(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.POST
        obj = Policy.objects.create(
            name=data['name'],
            description=data['description'],
            premium=data['premium'],
            duration_years=data['duration_years']
        )
        return HttpResponse('Object is created')
