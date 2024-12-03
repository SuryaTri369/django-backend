from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', views.employee_list, name='employee_list'),
    path('api/employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]