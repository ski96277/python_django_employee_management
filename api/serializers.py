from rest_framework import serializers
from .models import Company,Employee

#Create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        # fields = "__all__" 
        exclude = ['url']  # Exclude the URL field


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"
