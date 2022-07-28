from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class HandleApiView(APIView):
    def post(self, request):
        folder = Folder.objects.create()
        print(request.data)
        model_sr = FileListSerializer(data=request.data)
        if model_sr.is_valid(raise_exception=True):
            model_sr.save(folder=folder)
            return Response({'status_code': 200})
        return Response({'status_code': 400})

