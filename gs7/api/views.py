from django.http.response import HttpResponse
from django.shortcuts import render
import io
from  rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body  # we will save it in variable
        stream = io.BytesIO(json_data) # after that we will stream it
        pythondata = JSONParser().parse(stream) # convert to python data 
        id = pythondata.get('id',None) # if there is id go into if otherwise print directly all data
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data,content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type="application/json")
        

    def post(self,request,*args,**kwargs):
        json_data =request.body
        stream =io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'Msg':'Data Inserted'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    
    def put(self, request, *args, **kwargs):
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #complete update - require all data from Front /End
        # serializer = StudentSerializer(stu,data=pythondata)
        # partial Update - All data not required 
        serializer = StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'Msg':'Data updated'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)   


    def delete(self, request, *args, **kwargs):
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'Msg':'Data deleted'}
        return JsonResponse(res)





























