from rest_framework.test import APITestCase
from notesapp.models import NotesModel
class NotesAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NotesModel.objects.create(id=101,title="Python",description="Python is an easy programming language",author="Guido Van Rossum",status="Completed")
        with open("../output_revised.txt","w") as f:
            pass
    def test_get_request_for_all_records(self):
        url='http://127.0.0.1:8000/notes_crud/'
        response=self.client.get(url)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestForAllRecords=True\n")
                print("TestGetRequestForAllRecords = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestForAllRecords=False\n")
                print("TestGetRequestForAllRecords = Failed")

    def test_get_request_for_single_record(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.get(url)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestForSingleRecord=True\n")
                print("TestGetRequestForSingleRecord = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestForSingleRecord=False\n")
                print("TestGetRequestForSingleRecord = Failed")

    def test_get_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/102123/'#Non existing id
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        if response.status_code==404:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestFail=True\n")
                print("TestGetRequestFail = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestGetRequestFail=False\n")
                print("TestGetRequestFail = Failed")

    def test_post_request(self):
        url='http://127.0.0.1:8000/notes_crud/'
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language',
            'status':'completed'
        }
        response=self.client.post(url,data,format='json')
        #self.assertEqual(response.status_code,201)
        if response.status_code==201:
            with open("../output_revised.txt","a") as f:
                f.write("TestPostRequest=True\n")
                print("TestPostRequest = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPostRequest=False\n")
                print("TestPostRequest = Failed")

    def test_post_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/'
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language'
            #'status':'completed'   #skip status field to create
        }
        response=self.client.post(url,data,format='json')
        #self.assertEqual(response.status_code,400)
        if response.status_code==400:
            with open("../output_revised.txt","a") as f:
                f.write("TestPostRequestFail=True\n")
                print("TestPostRequestFail = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPostRequestFail=False\n")
                print("TestPostRequestFail = Failed")

    def test_put_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/' #existing id
        data={
                'title':'Java',
                'author':'Games Gosling',
                'description':'Python is a programming language',
                'status':'completed'
            }
        response=self.client.put(url,data,format='json')
        #self.assertEqual(response.status_code,200)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestPutRequest=True\n")
                print("TestPutRequest = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPutRequest=False\n")
                print("TestPutRequest = Failed")

    def test_put_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud_pk/12345/' #non existing id
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language',
            'status':'completed'
        }
        response=self.client.put(url,data,format='json')
        #self.assertEqual(response.status_code,500)
        #print(response.status_code)
        if response.status_code==500:
            with open("../output_revised.txt","a") as f:
                f.write("TestPutRequestFail=True\n")
                print("TestPutRequestFail = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPutRequestFail=False\n")
                print("TestPutRequestFail = Failed")

    def test_patch_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/' #existing id
        data={
                'status':'completed'
            }
        response=self.client.patch(url,data,format='json')
        #self.assertEqual(response.status_code,200)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestPatchRequest=True\n")
                print("TestPatchRequest = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPatchRequest=False\n")
                print("TestPatchRequest = Failed")

    def test_patch_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud_pk/12345/' #non existing id
        data={
            'status':'completed'
           }
        response=self.client.patch(url,data,format='json')
        #self.assertEqual(response.status_code,500)
        #print(response.status_code)
        if response.status_code==500:
            with open("../output_revised.txt","a") as f:
                f.write("TestPatchRequestFail=True\n")
                print("TestPatchRequestFail = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestPatchRequestFail=False\n")
                print("TestPatchRequestFail = Failed")

    def test_delete_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.delete(url)
        #self.assertEqual(response.status_code,200)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestDeleteRequest=True\n")
                print("TestDeleteRequest = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestDeleteRequest=False\n")
                print("TestDeleteRequest = Failed")

    def test_delete_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/10232/' #Non existing id
        response=self.client.delete(url)
        #self.assertEqual(response.status_code,404)
        if response.status_code==404:
            with open("../output_revised.txt","a") as f:
                f.write("TestDeleteRequestFail=True\n")
                print("TestDeleteRequestFail= Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestDeleteRequestFail=False\n")
                print("TestDeleteRequestFail=Failed")

    def test_search_by_id(self):
        url='http://127.0.0.1:8000/search_by_id/?id=101'
        response=self.client.get(url)
        #print(response.status_code)
        #self.assertEqual(response.status_code,404)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchById=True\n")
                print("TestSearchById = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchById=False\n")
                print("TestSearchById = Failed")

    def test_search_by_author(self):
        url='http://127.0.0.1:8000/search_by_author/?author=Guido Van Rossum'
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchByAuthor=True\n")
                print("TestSearchByAuthor = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchByAuthor=False\n")
                print("TestSearchByAuthor = Failed")

    def test_search_by_status(self): #Note executing
        url='http://127.0.0.1:8000/search_by_status/?status=Completed'
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        if response.status_code==200:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchByStatus=True\n")
                print("TestSearchByStatus = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestSearchByStatus=False\n")
                print("TestSearchByStatus = Failed")
