from rest_framework import serializers
from EmployeeApp.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'DepartmentName')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'EmployeeName', 'Department',
                  'DateOfJoining', 'PhotoFileName')
