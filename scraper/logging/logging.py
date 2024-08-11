import os
from datetime import datetime
from typing import Optional

class FlikartLogger:
    def __init__(self, log_line_name: str):
        """
        Initializes the logger with a specified log file name.
        
        :param log_line_name: Name of the log file (without extension).
        """
        self.logfile = os.path.join('logs', log_line_name + '.txt')
        self.current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _write_log(self, level: str, message: str) -> None:
        """
        Writes a log message to the file.
        
        :param level: The log level (INFO, ERROR, etc.).
        :param message: The message to write in the log file.
        """
        try:
            with open(self.logfile, 'a+') as logs:
                logs.write(f'{level} [{self.current_date}]: {message}.\n')
        except Exception as e:
            print(f"Logging failed: {e}")
            with open(self.logfile, 'w') as logs:
                logs.write(f'{level} [{self.current_date}]: {message}.\n')

    def info(self, message: str) -> None:
        """
        Logs an INFO level message.
        
        :param message: Message to write in the log file.
        """
        self._write_log('INFO', message)

    def error(self, message: str) -> None:
        """
        Logs an ERROR level message.
        
        :param message: Message to write in the log file.
        """
        self._write_log('ERROR', message)
