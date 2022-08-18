from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# from rest_framework.filters import SearchFilter

# Create your views here.


# ordering filter 
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields  = ['city']
    ordering_fields  = ['name', 'city']





"""
1) '^' starts with search
2) '=' Exact match
3) '@' Full-text search (currently only Supported Django PostgreSQL Backend)
4)'$' Regex search

"""


# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends = [SearchFilter]
#     # search_fields  = ['city']
#     search_fields  = ['^name']


# # search filter 
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends = [SearchFilter]
#     # search_fields  = ['city']
#     search_fields  = ['name', 'city']



# # locally filter
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends =[DjangoFilterBackend]
#     filterset_fields= ['city','name']



# Filter Globally 
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filterset_fields= ['city']




# One way of filtering  in a normal way

# class StudentList(ListAPIView):
#     # queryset=Student.objects.filter(passby = 'Nimish')
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(passby = user)