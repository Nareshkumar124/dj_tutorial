from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.


def studentsView(request: WSGIRequest):
    """
    View to handle student data.
    """
    students = Student.objects.all()
    students = students.values('student_id', 'name', 'branch')
    return JsonResponse(list(students), safe=False, json_dumps_params={'indent': 2})