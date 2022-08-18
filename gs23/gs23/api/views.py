from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
# from .paginations import MyPageNumberPagination
# from .paginations import MyLimitOffsetPagination
from .paginations import MyCursorPagination

from .models import Student

# Create your views here.


#  cursur paginations 
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class = MyCursorPagination



# #  Offset paginations 
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     pagination_class = MyLimitOffsetPagination


# # Local Paginations
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     pagination_class = MyPageNumberPagination


# Global Paginations
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


