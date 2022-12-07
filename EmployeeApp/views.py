from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeesSerializer
# Create your views here.


@csrf_exempt
def departementApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departement_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departement_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        departement_data = JSONParser().parse(request)
        departement = Departments.objects.get(
            id=departement_data['id'])
        departement_serializer = DepartmentSerializer(
            departement, data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed")
    elif request.method == "DELETE":
        departement = Departments.objects.get(id=id)
        departement.delete()


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employees.objects.all()
        employee_serializer = EmployeesSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeesSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            id=employee_data['id'])
        employee_serializer = EmployeesSerializer(
            employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed")
    elif request.method == "DELETE":
        employee = Employees.objects.get(id=id)
        employee.delete()
