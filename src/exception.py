# To handle Exceptions

# import sys
# import logging
# import traceback as tb

# def error_show(error, error_details:sys): # This function will be showing the error
#     exc_tb = error_details.exc_info()
#     filename = exc_tb.tb_frame.f_code.co_filename
#     error_message = f'Error occured in Python Script {0}, Line Number {1}, Error message {2}'
#     filename, exc_tb.tb_lineno, str(error)
# #      {0}          {1}             {2}

#     return error_message

# class customException(Exception):
#     def __init__(self, error_message, error_details:sys):
#         super().__init__(error_message)
#         self.error_message = error_show(error_message, error_details = error_details)

#     def __str__(self):
#         return self.error_message
    
# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by Zero!')
#         raise customException(e,sys)
import sys
import traceback
import logging

def error_show(error, error_details):
    exc_type, exc_value, exc_tb = error_details
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error occurred in Python Script {filename}, Line Number {exc_tb.tb_lineno}, Error message {str(error)}'
    return error_message

class customException(Exception):
    def __init__(self, error, error_details):
        super().__init__(str(error))
        self.error_message = error_show(error, error_details)

    def __str__(self):
        return self.error_message
    
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by Zero!')
        raise customException(e, sys.exc_info())

