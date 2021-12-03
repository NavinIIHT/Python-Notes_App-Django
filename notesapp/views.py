from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from notesapp.serializers import NotesSerializer
from notesapp.models import NotesModel
from notesapp.exceptions import IdNotAvailable,StatusNotAvailable,AuthorNotAvailable
from notesapp.service import NotesService

class NotesCRUDView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=NotesModel.objects.filter(id=id)
            if qs:
                serializer=NotesSerializer(qs,many=True)# converts qs to python dict.
                return Response(serializer.data)# converts python data to json and returns
            else:
                raise IdNotAvailable()
        qs=NotesModel.objects.all()
        serializer=NotesSerializer(qs,many=True)# converts qs to python dict.
        return Response(serializer.data)# convert
    def post(self, request,format=None):
        serializer=NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Note created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,format=None):
        id=pk
        try:
            note=NotesModel.objects.get(id=id)
            serializer=NotesSerializer(note,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Note updated"})
        except NotesModel.DoesNotExist:
            raise IdNotAvailable()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        try:
            note=NotesModel.objects.get(id=pk)
            serializer=NotesSerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Partial Note data updated"})
        except NotesModel.DoesNotExist:
            raise IdNotAvailable()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        #id=pk
        qs=NotesModel.objects.filter(id=pk).delete()
        if qs[0]==1:
            return Response({"msg":"Note deleted"})
        raise IdNotAvailable()

#Filtering
class SearchNotesByIdView(ListAPIView):
    serializer_class =NotesSerializer
    def get_queryset(self):
        id=self.request.GET.get('id')
        if id is not None:
            qs = NotesService.search_by_id(id)
            if qs:
                return qs
            else:
                raise IdNotAvailable()

class SearchNotesByAuthorView(ListAPIView):
    serializer_class =NotesSerializer
    def get_queryset(self):
        name=self.request.GET.get('author')
        if name is not None:
            qs = NotesService.search_by_author(name)
            if qs:
                return qs
            else:
                raise AuthorNotAvailable()

class SearchNotesByStatusView(ListAPIView):
    serializer_class =NotesSerializer
    def get_queryset(self):
        status=self.request.GET.get('status')
        if status is not None:
            qs = NotesService.search_by_status(status)
            if qs:
                return qs
            else:
                raise StatusNotAvailable()
