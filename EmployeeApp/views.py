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
        departement_data = JSONParser().parse(request)
        departement_serializer = DepartmentSerializer(data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save
            return JsonResponse("Added Success", safe=False)
        return JsonResponse("Failde to Add", safe=False)
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
        return JsonResponse("delete success", safe=False)
