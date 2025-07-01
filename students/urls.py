from django.urls import path
from . import views


urlpatterns = [
    # Api endpoint for students
    path('',views.studentsView,name='students'),
    path('<int:student_id>/', views.get_update_and_delete_single_student, name='get_single_student'),
]


