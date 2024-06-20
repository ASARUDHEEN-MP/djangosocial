from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 

class TestView(APIView):
    permission_classes = [AllowAny] 
    def get(self, request):
        return Response("hello")
    
class newcheck(APIView):
    def get(self,request):
        return Response("hellooo world test case here")

