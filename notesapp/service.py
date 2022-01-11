from notesapp.models import NotesModel
class NotesService:
    def search_by_id(id):
        qs=NotesModel.objects.all()
        qs=qs.filter(id=id)
        return qs
    def search_by_author(name):
        qs=NotesModel.objects.all()
        qs=qs.filter(author=name)
        return qs
    def search_by_status(status):
        qs=NotesModel.objects.all()
        qs=qs.filter(status=status)
        return qs
