from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404 #when objects doesn't exist
from rest_framework.views import APIView #Normal view can return API data
from rest_framework.response import Response # response
from rest_framework import status
from .models import employees
from . serializers import employeesSerializer


class employeeList(APIView):

    def get(self, request):
        employee1 = employees.objects.all()
        serializer=employeesSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self):
        pass







