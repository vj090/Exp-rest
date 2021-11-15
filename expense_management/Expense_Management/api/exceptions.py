from rest_framework.exceptions import APIException


class DuplicateMonth(APIException):
    """
    Created custom Error for the Api page
    """
    status_code = 400
    default_detail = "Month Already exist"
    default_code = "unreadable"
