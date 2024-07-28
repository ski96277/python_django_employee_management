from django.shortcuts import render
from rest_framework import viewsets
from .models import Company , Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    #Get all employees of a company by id
    # api/v1/companies/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk = pk) 
            emps = Employee.objects.filter(company=company)
            emps_serializaer = EmployeeSerializer(emps,many = True,context={'request': request})
            return Response(emps_serializaer.data)
        except Exception as e:
            return Response({"details":f"Company profile ({pk}) not found"})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset  = Employee.objects.all()
    serializer_class = EmployeeSerializer
