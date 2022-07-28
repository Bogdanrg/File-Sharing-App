from rest_framework import serializers
from .models import *


class FileListSerializer(serializers.Serializer):
    file = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, max_length=10000, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def create(self, validated_data):
        files = validated_data.get('file')
        folder = validated_data.get('folder')
        file_objs = []
        for file in files:
            file_obj = File.objects.create(file=file, folder=folder)
            file_objs.append(file_obj)

        return (i for i in file_objs)

    class Meta:
        model = File
        fields = ['id', 'file', 'folder', 'created_at']
