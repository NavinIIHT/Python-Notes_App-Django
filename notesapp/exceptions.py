
from rest_framework.exceptions import APIException
class IdNotAvailable(APIException):
    default_detail = 'Specified note id is not available'

class AuthorNotAvailable(APIException):
    default_detail = 'Specified note author is not available'

class StatusNotAvailable(APIException):
    default_detail = 'Specified note status is not available'
