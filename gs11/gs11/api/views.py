from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView



class NimishLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer



class NimishRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer




# class NimishList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer


# class NimishCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer



# class NimishRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer




# class NimishUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer



# class NimishDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer



# class NimishLC(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer



# class NimishRU(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer


# class NimishRD(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer



# class NimishRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer
