from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    # path('',views.Employees.as_view()),
    # path("<int:pk>/", views.EmployeeDetail.as_view())
    path('',include(router.urls))
]
