
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from notesapp.views import NotesCRUDView,SearchNotesByIdView,SearchNotesByAuthorView,SearchNotesByStatusView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes_crud/',NotesCRUDView.as_view()),
    path('notes_crud_pk/<int:pk>/',NotesCRUDView.as_view()),
    url(r'^search_by_id/',SearchNotesByIdView.as_view()),
    url(r'^search_by_author/',SearchNotesByAuthorView.as_view()),
    url(r'^search_by_status/',SearchNotesByStatusView.as_view()),
]
