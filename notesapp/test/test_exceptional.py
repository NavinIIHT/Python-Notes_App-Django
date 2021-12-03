from rest_framework.test import APITestCase
from notesapp.models import NotesModel
class NotesAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NotesModel.objects.create(id=101,title="Python",description="Python is an easy programming language",author="Guido Van Rossum",status="Completed")
        with open("../output_exception_revised.txt","w") as f:
            pass
    def test_search_by_id_fail(self):
        url='http://127.0.0.1:8000/search_by_id/?id=1234'
        response=self.client.get(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByIdFail=True\n")
                print("TestSearchByIdFail =Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByIdFail=False\n")
                print("TestSearchByIdFail = Failed")

    def test_search_by_author_fail(self):
        url='http://127.0.0.1:8000/search_by_author/?author=xyz'
        response=self.client.get(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByAuthorFail=True\n")
                print("TestSearchByAuthorFail = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByAuthorFail=False\n")
                print("TestSearchByAuthorFail = Failed")

    def test_search_by_status_fail(self):
        url='http://127.0.0.1:8000/search_by_status/?status=cmpltd'
        response=self.client.get(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByStatusFail=True\n")
                print("TestSearchByStatusFail = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByStatusFail=False\n")
                print("TestSearchByStatusFail = Failed")

    def test_id_not_available_error_at_get_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/102111/'
        response=self.client.get(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtGetRequest=True\n")
                print("TestIdNotAvailableErrorAtGetRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtGetRequest=False\n")
                print("TestIdNotAvailableErrorAtGetRequest = Failed")

    def test_id_not_available_error_at_put_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.put(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPutRequest=True\n")
                print("TestIdNotAvailableErrorAtPutRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPutRequest=False\n")
                print("TestIdNotAvailableErrorAtPutRequest = Failed")

    def test_id_not_available_error_at_patch_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.patch(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPatchRequest=True\n")
                print("TestIdNotAvailableErrorAtPatchRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPatchRequest=False\n")
                print("TestIdNotAvailableErrorAtPatchRequest = Failed")

    def test_id_not_available_error_at_delete_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.delete(url)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtDeleteRequest=True\n")
                print("TestIdNotAvailableErrorAtDeleteRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtDeleteRequest=False\n")
                print("TestIdNotAvailableErrorAtDeleteRequest = Failed")
