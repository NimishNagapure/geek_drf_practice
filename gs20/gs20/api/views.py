from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import StudentRateThrottle
# Session Authentications

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,StudentRateThrottle]
    throttle_classes = [AnonRateThrottle,UserRateThroStudentRateThrottlettle]



    