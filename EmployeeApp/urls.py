from django.urls import path, re_path
from EmployeeApp import views

urlpatterns = [
    re_path(r'^department$', views.departementApi),
    re_path(r'^department/([0-9]+)$', views.departementApi)
]
