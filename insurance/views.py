from django.shortcuts import render,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from insurance.models import Policy
from .serializers import PolicySerializers
from rest_framework.response import Response
# Create your views here.
# insurance/views.py


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Policy, PurchasedPolicy

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'insurance/policy_list.html', {'policies': policies})

@login_required
def purchase_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    PurchasedPolicy.objects.create(user=request.user, policy=policy)
    return redirect('my_policies')

@login_required
def my_policies(request):
    purchased_policies = PurchasedPolicy.objects.filter(user=request.user)
    return render(request, 'insurance/my_policies.html', {'purchased_policies': purchased_policies})

#API

class API(GenericAPIView):

    serializer_class=PolicySerializers
    def get(self,request):
        objects=Policy.objects.all()
        serializer= PolicySerializers(objects,many=True)

        return Response(serializer.data)

    def post(self, request):
        data=request.POST
        obj=Policy.objects.create(name=data['name'],description=data['description'],premium=data['premium'],duration_years=data['duration_years'])

        return HttpResponse('object is created ')

