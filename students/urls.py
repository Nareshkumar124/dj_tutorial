from django.urls import path
from . import views


urlpatterns = [
    # Api endpoint for students
    path('',views.studentsView,name='students'),
]