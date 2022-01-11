from rest_framework.test import APITestCase
from notesapp.models import NotesModel
#from notesapp.exceptions import IdNotAvailable,AuthorNotAvailable,StatusNotAvailable
class NotesAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NotesModel.objects.create(id=101,title="Python",description="Python is an easy programming language",author="Guido Van Rossum",status="Completed")
        with open("../output_exception_revised.txt","w") as f:
            pass
    def test_search_by_id_fail(self):
        url='http://127.0.0.1:8000/search_by_id/?id=1234'#Non existing id
        response=self.client.get(url)
        #print("1",response.status_code)
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
        #print("2",response.status_code)
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
        #print("3",response.status_code)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByStatusFail=True\n")
                print("TestSearchByStatusFail = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestSearchByStatusFail=False\n")
                print("TestSearchByStatusFail = Failed")

    def test_id_not_available_error_at_get_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/102111/'#slash must
        response=self.client.get(url)
        #print("4",response.status_code)
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
        #print("5",response.status_code)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPutRequest=True\n")
                print("TestIdNotAvailableErrorAtPutRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPutRequest=False\n")
                print("TestIdNotAvailableErrorAtPutRequest = Failed")

    def test_id_not_available_error_at_patch_request(self): #ok
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.patch(url)
        #print("6",response.status_code)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPatchRequest=True\n")
                print("TestIdNotAvailableErrorAtPatchRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtPatchRequest=False\n")
                print("TestIdNotAvailableErrorAtPatchRequest = Failed")

    def test_id_not_available_error_at_delete_request(self): #ok
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.delete(url)
        #print("7",response.status_code)
        if response.status_code==500:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtDeleteRequest=True\n")
                print("TestIdNotAvailableErrorAtDeleteRequest = Passed")
        else:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestIdNotAvailableErrorAtDeleteRequest=False\n")
                print("TestIdNotAvailableErrorAtDeleteRequest = Failed")



# test cases with try and except blocks

    # def test_search_by_id_fail(self): #1
    #     url='http://127.0.0.1:8000/search_by_id/?id=1234'#Non existing id
    #     try:
    #         response=self.client.get(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByIdFail=False\n")
    #             print("TestSearchByIdFail = Failed")
    #     except IdNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByIdFail=True\n")
    #             print("TestSearchByIdFail =Passed")
    #
    # def test_search_by_author_fail(self):#2
    #     url='http://127.0.0.1:8000/search_by_author/?author=xyz'
    #     try:
    #         response=self.client.get(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByAuthorFail=True\n")
    #             print("TestSearchByAuthorFail = Passed")
    #     except AuthorNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByAuthorFail=False\n")
    #             print("TestSearchByAuthorFail = Failed")
    #
    # def test_search_by_status_fail(self):#3
    #     url='http://127.0.0.1:8000/search_by_status/?status=cmpltd'
    #     try:
    #         response=self.client.get(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByStatusFail=True\n")
    #             print("TestSearchByStatusFail = Passed")
    #     except StatusNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestSearchByStatusFail=False\n")
    #             print("TestSearchByStatusFail = Failed")
    #
    # def test_id_not_available_error_at_get_request(self):#4
    #     url='http://127.0.0.1:8000/notes_crud_pk/102111/'  #slash must
    #     try:
    #         response=self.client.get(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtGetRequest=True\n")
    #             print("TestIdNotAvailableErrorAtGetRequest = Passed")
    #     except IdNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtGetRequest=False\n")
    #             print("TestIdNotAvailableErrorAtGetRequest = Failed")
    #
    # def test_id_not_available_error_at_put_request(self):#5
    #     url='http://127.0.0.1:8000/notes_crud_pk/11234/'  #slash must
    #     try:
    #         response=self.client.put(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtPutRequest=True\n")
    #             print("TestIdNotAvailableErrorAtPutRequest = Passed")
    #     except IdNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtPutRequest=False\n")
    #             print("TestIdNotAvailableErrorAtPutRequest = Failed")
    #
    # def test_id_not_available_error_at_patch_request(self):#6
    #     url='http://127.0.0.1:8000/notes_crud_pk/11234/'  #slash must
    #     try:
    #         response=self.client.patch(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtPatchRequest=True\n")
    #             print("TestIdNotAvailableErrorAtPatchRequest = Passed")
    #     except IdNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtPatchRequest=False\n")
    #             print("TestIdNotAvailableErrorAtPatchRequest = Failed")
    #
    # def test_id_not_available_error_at_delete_request(self):
    #     url='http://127.0.0.1:8000/notes_crud_pk/11234/'  #slash must
    #     try:
    #         response=self.client.delete(url)
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtDeleteRequest=True\n")
    #             print("TestIdNotAvailableErrorAtDeleteRequest = Passed")
    #     except IdNotAvailable:
    #         with open("../output_exception_revised.txt","a") as f:
    #             f.write("TestIdNotAvailableErrorAtDeleteRequest=False\n")
    #             print("TestIdNotAvailableErrorAtDeleteRequest = Failed")
