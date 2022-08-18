from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer 
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse , JsonResponse
# Create your views here.

# Model object - single student data model

def student_detail(request,pk):
    stu = Student.objects.get(id= pk)   # Created Model Object
    # print(stu)
    serializer = StudentSerializer(stu)  # converted to python object
    # print(serializer)
    # json_data = JSONRenderer().render(serializer.data)  # then we converted into json 
    # print(json_data)
    # return HttpResponse(json_data,content_type="application/json")  # after that sent to client 

    return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()   # Created Model Object
    # print(stu)
    serializer = StudentSerializer(stu, many= True)  # converted to python object
    # print(serializer)
    # json_data = JSONRenderer().render(serializer.data)  # then we converted into json 
    # print(json_data)
    # return HttpResponse(json_data,content_type="application/json")  # after that sent to client 

    return JsonResponse(serializer.data,safe=False)
