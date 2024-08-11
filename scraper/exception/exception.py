import os
import sys
from types import TracebackType
from typing import Optional

def error_message_details(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information, including the script name, line number, and error message.

    Args:
        error (Exception): The exception object that was raised.
        error_detail (sys): The sys module, which provides access to exception details.

    Returns:
        str: A formatted string containing the error details, including the script name, 
             line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    if isinstance(exc_tb, TracebackType):
        file_name: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]  # Get the script file name
        error_message: str = (
            f"Error occurred in Python script: [{file_name}] "
            f"at line number: [{exc_tb.tb_lineno}], "
            f"with error message: [{str(error)}]"
        )
        return error_message
    return "No traceback available for this error."

class FilpkartException(Exception):
    """
    Custom exception for handling errors in the Flipkart scraper.

    Args:
        error_message (str): A descriptive error message.
        error_detail (sys): The sys module to access exception details.
    """
    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
    
    def __str__(self) -> str:
        return self.error_message