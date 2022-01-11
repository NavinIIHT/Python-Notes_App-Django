"""NotesAppAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notesapp.views import NotesCRUDView,SearchNotesByIdView,SearchNotesByAuthorView,SearchNotesByStatusView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes_crud/',NotesCRUDView.as_view()),
    path('notes_crud_pk/<int:pk>/',NotesCRUDView.as_view()),

    #url not working
    # url(r'^search_by_id/',SearchNotesByIdView.as_view()),
    # url(r'^search_by_author/',SearchNotesByAuthorView.as_view()),
    # url(r'^search_by_status/',SearchNotesByStatusView.as_view()),

    path('search_by_id/',SearchNotesByIdView.as_view()),
    path('search_by_author/',SearchNotesByAuthorView.as_view()),
    path('search_by_status/',SearchNotesByStatusView.as_view()),

]
