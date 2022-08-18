from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Session Authentications

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes =[IsAuthenticated]
    permission_classes =[IsAuthenticatedOrReadOnly]
    


#  http http://127.0.0.1:8000/stdapi/
# http http://127.0.0.1:8000/stdapi/ 'Authorization:Token 9ab93a110ad7d47f2f1919038c13f84e25b32cba'
# http -f POST http://127.0.0.1:8000/stdapi/ name=Shantanu roll=104 city=Dhanbad  'Authorization:Token 9ab93a110ad7d47f2f1919038c13f84e25b32cba'
# http PUT  http://127.0.0.1:8000/stdapi/4/ name=Donni roll=104 city=Banglore  'Authorization:Token 9ab93a110ad7d47f2f1919038c13f84e25b32cba'
# http DELETE  http://127.0.0.1:8000/stdapi/4/ 'Authorization:Token 9ab93a110ad7d47f2f1919038c13f84e25b32cba'