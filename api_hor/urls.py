
from django.contrib import admin
from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('get_employees', views.EmpApiView.as_view()),
]
