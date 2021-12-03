from django.db import models

class NotesModel(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=20,null=False)
    description=models.CharField(max_length=200,null=False)
    author=models.CharField(max_length=20,null=False)
    status=models.CharField(max_length=20,null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
