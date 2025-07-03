from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,mixins,generics,viewsets

from .serializers import EmployeeSerializer
from .models import Employee


## API VIEW
# # Create your views here.
# class Employees(APIView):
    
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request:WSGIRequest):
#         data = request.data
#         serializer = EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# class EmployeeDetail(APIView):

#     def get_employee(self,emp_id:int):
#         try:
#             return Employee.objects.get(emp_id=emp_id)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request:WSGIRequest,emp_id:int):
#         employee = self.get_employee(emp_id=emp_id)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request:WSGIRequest,emp_id:int):
#         employee = self.get_employee(emp_id)
#         serializer = EmployeeSerializer(employee,data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request:WSGIRequest,emp_id:int):
#         employee = self.get_employee(emp_id)
#         employee.delete()
#         return Response("deleted",status=status.HTTP_204_NO_CONTENT)
    

        
    

## Mixins       
# class Employees(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    

class EmployeeDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    

## Generics
# class Employees(
#     generics.ListAPIView,
#     generics.CreateAPIView
# ):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


# class EmployeeDetail(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


class Employees(
    generics.ListCreateAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'    


class EmployeeViewSet(
    # viewsets.ViewSet
    viewsets.ModelViewSet
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    # def list(self,request):
    #     queryset = Employee.objects.all()
    #     serializer = EmployeeSerializer(queryset, many = True)
    #     return Response(serializer.data)
    
    # def create(self,request):
    #     serializer = EmployeeSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    
    
        

            
