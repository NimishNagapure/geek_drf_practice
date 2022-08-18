from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Session Authentications

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    


# http POST http://127.0.0.1:8000/gettoken/ username='admin' password='admin'
#  http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODkyMzIzLCJqdGkiOiI1N2I1YTI1ZDNlYWU0ZmI2OGE5MWMyMTBiZjcyMjhlOCIsInVzZXJfaWQiOjF9.4fcEc7VuoNOf5HSHIPBJP1HSI_ledOl-YLQhV0T7Wuo"
# http http://127.0.0.1:8000/stdapi/
# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNTk3ODQyMywianRpIjoiZmMxMjgxMTBkZTdkNDg4NGIxNzBmODdmNDdiMjNhZDYiLCJ1c2VyX2lkIjoxfQ.UE9sT2cn1Sr0ZHdLWvp6YpQ_o6YHkucBHnQPoxtMRT0"
# http http://127.0.0.1:8000/stdapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODkzNTA2LCJqdGkiOiJlODY1ZmQzMjJjMGI0ZjMyOWIzNTM5Y2IxMmE0NGY5ZiIsInVzZXJfaWQiOjF9.0idP2HUXkvHSwFuZnc_eYRz1B0qQt2i5KvHxxrZAhJY'
# http -f POST  http://127.0.0.1:8000/stdapi/ name=Coolboy roll=104 city=Ranchi 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODk0MzM2LCJqdGkiOiJhMDk3ODJkOWQxYzU0ZjZlYjkyYzgxODhjNGI2ZDdmNSIsInVzZXJfaWQiOjF9.zhElN2V7IhTNjXEMgHpaxmOTMcDwl_LfrV5HsCKiu4s'
# http PUT http://127.0.0.1:8000/stdapi/2/ name=Chetan roll=104 city=Pune 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODk0MzM2LCJqdGkiOiJhMDk3ODJkOWQxYzU0ZjZlYjkyYzgxODhjNGI2ZDdmNSIsInVzZXJfaWQiOjF9.zhElN2V7IhTNjXEMgHpaxmOTMcDwl_LfrV5HsCKiu4s'
# http DELETE http://127.0.0.1:8000/stdapi/5/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODk0ODE4LCJqdGkiOiIzNThmNWRlZjU0MDU0NTY0YmMwYjE0NmYwNTJmN2YyZCIsInVzZXJfaWQiOjF9.xi9dedKspx5-LkbmGOC_p5SfoYNH_ShwWKtUVRkt_HY'