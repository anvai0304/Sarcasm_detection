# To handle Exceptions

import sys

def error_show(error, error_details:sys): # This function will be showing the error
    exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error occured in Python Script {0}, Line Number {1}, Error message {2}'
    filename, exc_tb.tb_lineno, str(error)
#      {0}          {1}             {2}

    return error_message

class customException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_show(error_message, error_details = error_details)

    def __str__(self):
        return self.error_message
