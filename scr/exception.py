import sys

# def error details(exc_type, exc_value, exc_traceback):
#     """Prints the error details to stderr."""
#     if issubclass(exc_type, KeyboardInterrupt):
#         sys.__excepthook__(exc_type, exc_value, exc_traceback)
#         return

#     # Print the error details to stderr
#     print(f"Error: {exc_value}", file=sys.stderr)
def error_details(error, error_detail:sys):
    """Prints the error details to stderr."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]".format(
    file_name,
    line_number,
    exc_tb.tb_lineno,
    str(error)    
    )
    return error_message

class CustomException(Exception):
    """Custom exception class that inherits from the built-in Exception class."""
    def __init__(self, error_message: str, error_detail: sys):
        """Initializes the CustomException with an error message and error details."""
        super().__init__(error_message)
        self.error_message = error_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        """Returns the string representation of the CustomException."""
        return self.error_message