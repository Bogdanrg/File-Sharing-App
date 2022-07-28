import uuid as uuid
from django.db import models


class Folder(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)


def user_directory_path(instance, filename):
    return f'photos/{instance.folder.uuid}/{filename}'


class File(models.Model):
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    created_at = models.DateField(auto_now=True)
