# from django.http.response import HttpResponseServerError
from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':   # true
        json_data = request.body  # whatever data comning we have save in variable 
        stream = io.BytesIO(json_data)       # converted body into json parser
        pythondata = JSONParser().parse(stream) #convverted into python native 
        serializer = StudentSerializer(data=pythondata)    # converted into complex data serial
        if serializer.is_valid():  # check if the complex data is valid to save in db
            serializer.save()
            res = {'msg':'Data Inserted'} 
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res)

        return JsonResponse(serializer.errors)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type='application/json')     

        


