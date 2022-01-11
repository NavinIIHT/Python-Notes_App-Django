# API Serializer
from rest_framework.serializers import ModelSerializer
from notesapp.models import NotesModel
class NotesSerializer(ModelSerializer):
    class Meta:
        model=NotesModel
        fields='__all__'
