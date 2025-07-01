from django.http import JsonResponse
from .models import Student
from django.core.handlers.wsgi import WSGIRequest
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def studentsView(request: WSGIRequest):
    '''Handle GET and POST requests for students.'''
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        # Validate the serializer data
        # If the data is valid, save the new student
        # If the data is invalid, return an error response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def get_update_and_delete_single_student(request: WSGIRequest, student_id: int):
    '''Retrieve a single student by ID.'''

    student = Student.get_student_by_id(student_id)
    if student is None:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    
    if request.method == 'PUT':
        # get data from request and validate
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            updated_student=student.update_single_student(serializer.data)
            return Response({
                "status":"success",
                "data": StudentSerializer(updated_student).data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    

    if request.method == 'DELETE':
        student.delete()
        return Response({"status":"success"},status=status.HTTP_204_NO_CONTENT)
    








