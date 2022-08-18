from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class NimishList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstd'


class NimishCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystd'




class NimishRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstd'





class NimishUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystd'




class NimishDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystd'


