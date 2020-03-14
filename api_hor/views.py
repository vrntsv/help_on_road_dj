from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.forms.models import model_to_dict
import site_backend.models as models


class EmpApiView(APIView):
    def get(self, request):
        employees = models.Employees.objects.all().values()
        return Response({"employees": employees})