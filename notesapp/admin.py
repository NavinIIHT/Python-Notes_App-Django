from django.contrib import admin
from .models import NotesModel
class AdminNotesModel(admin.ModelAdmin):
    list_display=['id','title','description','author','status','created_date','updated_date']
admin.site.register(NotesModel,AdminNotesModel)
