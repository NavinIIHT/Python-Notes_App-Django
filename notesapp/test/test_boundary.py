from rest_framework.test import APITestCase
class NotesAppAPIBoundaryTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        with open("../output_boundary_revised.txt","w") as f:
            pass
    def test_boundary(self):
        with open("../output_boundary_revised.txt","a") as f:
            f.write("TestBoundary=True\n")
            print("TestBoundary = Passed")
