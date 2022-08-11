from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import zipfile


class HandleApiView(APIView):
    def post(self, request):
        folder_name = request.data.get('folder')
        if folder_name:
            folder = Folder.objects.create(folder_name=folder_name)
        else:
            folder = Folder.objects.create()
        model_sr = FileListSerializer(data=request.data)
        if model_sr.is_valid(raise_exception=True):
            model_sr.save(folder=folder)
            model_sr.zip_files(folder)
            files = folder.file_set.all()
            return Response({'status_code': 200,
                             'data': {'folder': FolderSerializer(folder).data,
                                      'files': FileSerializer(files, many=True).data}})
        return Response({'status_code': 400})

    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response({'data': serializer.data})

