from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.serializers import LoginSerializer, RegisterSerializer, TaskInfoSerializer
from tasks.models import TaskInfo

from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination


                            # Function-based Views
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def taskInformation(request):
    if request.method == 'GET':
        tasks = TaskInfo.objects.all()
        
        # pagination 
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(tasks, request)
        
        serializer = TaskInfoSerializer(result_page, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        tasks = request.data
        serializer = TaskInfoSerializer(data = tasks)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        tasks = request.data
        obj = TaskInfo.objects.get(id = tasks['id'])
        serializer = TaskInfoSerializer(obj, data=tasks)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        tasks = request.data
        obj = TaskInfo.objects.get(id = tasks['id'])
        obj.delete()
        return Response({"message":"Task deleted"})
        

class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        _data = request.data
        serializer = RegisterSerializer(data = _data)
        
        if not serializer.is_valid():
            return Response({"message": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.save()
        return Response({"message":"User Created"}, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        _data = request.data
        serializer = LoginSerializer(data = _data)
        
        if not serializer.is_valid():
            return Response({"message":serializer.errors}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'])

        
        if not user:
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND)
        
        token,_ = Token.objects.get_or_create(user=user)
        
        return Response({'message': 'Login successfull', 'token':str(token)}, status=status.HTTP_200_OK)














































        
                            # Class-based Views
# from rest_framework.views import APIView

# class TaskInformationClass(APIView):
#     def get(self, request):
#         tasks = TaskInfo.objects.all()
#         serializer = TaskInfoSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         tasks = request.data
#         serializer = TaskInfoSerializer(data = tasks)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


                                # Viewsets
# from rest_framework import viewsets
# from rest_framework import status

# class TaskInfoViewSet(viewsets.ModelViewSet):
#      serializer_class = TaskInfoSerializer
#      queryset = TaskInfo.objects.all()
     
#      def list(self, request):
#         search = request.GET.get("search")
#         queryset = self.queryset
        
#         if search:
#             queryset = queryset.filter(title__startswith = search)
        
#         serializer = TaskInfoSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

        