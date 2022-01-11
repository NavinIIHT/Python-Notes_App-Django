from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from notesapp.serializers import NotesSerializer
from notesapp.models import NotesModel
from notesapp.exceptions import IdNotAvailable,StatusNotAvailable,AuthorNotAvailable
from notesapp.service import NotesService
#APIview with custom exception
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
        #qs=NotesModel.objects.filter(pk=id)#works
        #qs=NotesModel.objects.filter(id=id)# getting problem at saving
        try:
            note=NotesModel.objects.get(id=id) #Raising DoesNotExist/NotesModel object(117)
            serializer=NotesSerializer(note,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Note updated"})
        except NotesModel.DoesNotExist:
            raise IdNotAvailable()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        #id=pk
        #qs=NotesModel.objects.filter(pk=id)
        #qs=NotesModel.objects.filter(id=id)# getting problem at saving
        try:
            note=NotesModel.objects.get(id=pk) #Raising DoesNotExist/NotesModel object(117)
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
        id=self.request.GET.get('id')#getting field value from url
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



#----------------

#from .errors import NotAvailableError
# from django.shortcuts import render
# from django.views.generic import View
# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer

# import io
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# @method_decorator(csrf_exempt,name='dispatch')


#crud view with custom exception
# class NotesCRUDView(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pdata=JSONParser().parse(stream)#json to dict
#         id=pdata.get('id',None)
#         if id is not None:
#             note=NotesModel.objects.filter(id=id)
#             if not note:# empty qs
#                 raise IdNotAvailableError("Specified id of Note is not available")
#
#             # try:
#             #     note=NotesModel.objects.get(id=id)
#             # except NotesModel.DoesNotExist:
#             #     raise IdNotAvailableError("Specified id of Note is not available")
#                 # try:
#                 #     raise IdNotAvailableError("Specified id of Note is not available")
#                 # except IdNotAvailableError as e:
#                 #     #print(e.str)
#                 #     json_message=JSONRenderer().render({"msg":e.str})
#                 #     return HttpResponse(json_message,content_type="application/json")
#
#
#             # Normal error message
#                 # message={"message":"Specified id of Note does not exist"}
#                 # json_message=JSONRenderer().render(message)#dict to json
#                 # return HttpResponse(json_message,content_type="application/json")
#
#             # Without raising exception
#                 # msg=IdNotAvailableError("Specified id of Note does not exist")
#                 # json_message=JSONRenderer().render({"msg":msg.str})
#                 # return HttpResponse(json_message,content_type="application/json")
#
#             py_data=NotesSerializer(note)#Serialization
#             json_note_data=JSONRenderer().render(py_data.data)#dict to json
#             return HttpResponse(json_note_data,content_type="application/json")
#         qs=NotesModel.objects.all()
#         py_data=NotesSerializer(qs,many=True)#Serialization
#         json_note_data=JSONRenderer().render(py_data.data)#dict to json
#         return HttpResponse(json_note_data,content_type="application/json")
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         serializer=NotesSerializer(data=pydata)#Deserialization
#         if serializer.is_valid():
#             serializer.save()
#             message={'message':'Note created successfully'}
#             json_data=JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json',status=200)
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         id=pydata.get('id')
#         # try:
#         #     note=NotesModel.objects.filter(id=id)
#         # except NotesModel.DoesNotExist:
#         #     raise IdNotAvailableError("Specified id of Note is not available")
#         note=NotesModel.objects.filter(id=id)
#         if not note:# empty qs
#             raise IdNotAvailableError("Specified id of Note is not available to update")
#
#         #serializer=NotesSerializer(note,data=pydata)
#         serializer=NotesSerializer(note,data=pydata,partial=True)#partial or full updation
#         if serializer.is_valid():
#             serializer.save()
#             message={'message':'Note updated successfully'}
#             json_data=JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         id=pydata.get('id')
#         qs=NotesModel.objects.filter(id=id).delete()#qs
#         if qs[0]==1:
#             message={'message':'Note deleted successfully'}
#             json_data=JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')
#         else:
#             raise IdNotAvailableError("Specified id of Note is not available to delete")



#--
        # try:
        #     note=NotesModel.objects.get(id=id)
        #     note.delete()
        #     message={'message':'Note deleted successfully'}
        #     json_data=JSONRenderer().render(message)
        #     return HttpResponse(json_data,content_type='application/json')
        # except NotesModel.DoesNotExist:
        #     message={'message':'Specified id of Note is not available'}
        #     json_data=JSONRenderer().render(message)
        #     return HttpResponse(json_data,content_type='application/json')



#crud view without custom exception

# class NotesCRUDView(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pdata=JSONParser().parse(stream)#json to dict
#         id=pdata.get('id',None)
#         if id is not None:
#             try:
#                 note=NotesModel.objects.get(id=id)
#             except:
#                 message={"message":"Specified id of Note does not exist"}
#                 json_message=JSONRenderer().render(message)#dict to json
#                 return HttpResponse(json_message,content_type="application/json")
#             py_data=NotesSerializer(note)#Serialization
#             json_note_data=JSONRenderer().render(py_data.data)#dict to json
#             return HttpResponse(json_note_data,content_type="application/json")
#         qs=NotesModel.objects.all()
#         py_data=NotesSerializer(qs,many=True)#Serialization
#         json_note_data=JSONRenderer().render(py_data.data)#dict to json
#         return HttpResponse(json_note_data,content_type="application/json")
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         serializer=NotesSerializer(data=pydata)#Deserialization
#         if serializer.is_valid():
#             serializer.save()
#             message={'message':'Note created successfully'}
#             json_data=JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json',status=200)
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
#
#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         id=pydata.get('id')
#         note=NotesModel.objects.get(id=id)
#         #serializer=NotesSerializer(note,data=pydata)
#         serializer=NotesSerializer(note,data=pydata,partial=True)#partial or full updation
#         if serializer.is_valid():
#             serializer.save()
#             message={'message':'Note updated successfully'}
#             json_data=JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         id=pydata.get('id')
#         note=NotesModel.objects.get(id=id)
#         note.delete()
#         message={'message':'Note deleted successfully'}
#         json_data=JSONRenderer().render(message)
#         return HttpResponse(json_data,content_type='application/json')




# #APIview without custom exception
#
# class NotesCRUDView(APIView):
#     def get(self,request,pk=None,format=None):
#         id=pk
#         if id is not None:
#             qs=NotesModel.objects.get(id=id)
#             serializer=NotesSerializer(qs)# converts qs to python dict.
#             return Response(serializer.data)# converts python data to json and returns
#         qs=NotesModel.objects.all()
#         serializer=NotesSerializer(qs,many=True)# converts qs to python dict.
#         return Response(serializer.data)# convert
#     def post(self, request,format=None):
#         serializer=NotesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Note created"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def put(self,request,pk,format=None):
#         id=pk
#         qs=NotesModel.objects.get(pk=id)
#         serializer=NotesSerializer(qs,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Note updated"})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def patch(self,request,pk,format=None):
#         id=pk
#         qs=NotesModel.objects.get(pk=id)
#         serializer=NotesSerializer(qs,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Partial Note data updated"})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk,format=None):
#         id=pk
#         qs=NotesModel.objects.get(pk=id)
#         qs.delete()
#         return Response({"msg":"Note deleted"})
#
