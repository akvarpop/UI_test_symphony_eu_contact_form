from enum import Enum


class GlobalErrorMessage(Enum):
    CONTACT_FORM_NOT_SEND = 'Contact form not send'
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    USER_NOT_CREATE = 'User not found in file'
    USER_NOT_DELETE = 'User not delete'
    USER_NOT_CHANGE = 'Data users not change'
    INCORRECT_DATA = 'When entering incorrect data in the field, an error did not appear'
