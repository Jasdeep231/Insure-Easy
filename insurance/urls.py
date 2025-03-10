# insurance/urls.py

from django.urls import path
from insurance import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Insurance API",
      default_version='v1',
      description="Insurance",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('purchase/<int:policy_id>/', views.purchase_policy, name='purchase_policy'),
    path('my-policies/', views.my_policies, name='my_policies'),
    path('api/', views.API.as_view(), name='api-policies'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
