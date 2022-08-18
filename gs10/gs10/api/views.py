from .models import Student 
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


#pk is not required 

class NimishLC_API(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#pk is required


class NimishRUD_API(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)








# class NimishList_API(GenericAPIView,ListModelMixin):
#     queryset= Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class NimishCreate_API(GenericAPIView,CreateModelMixin):
#     queryset= Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class NimishRetrive_API(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class =StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class NimishUpdate_API(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class =StudentSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)



# class NimishDestroy_API(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class =StudentSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)