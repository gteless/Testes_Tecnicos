import datetime
import logging

'''
Logger
    Configure logging for the automation process. This module sets up both file-based and BotCity logging.
    - Creates dated log files in the output directory
    - Sets up logging format with timestamps
    - Configures BotCity's built-in Execution Log 
    - Provides a reusable logger instance

    Usage:
        Import the logger in other files with:
        logger = logging.getLogger(__name__)
        logger.info(f"Add your message including {variables}.")
'''


logger = logging.getLogger(__name__)


def log_result_file() -> str:
    """
    Returns the path to the log file.
    """
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_result_file = f".\\log\\Log_{date}.txt"
    return log_result_file


def setup_logger():
    """
    Setups Python logger.
    """
    log_file = log_result_file()
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        encoding='utf-8'
                        )
    logger.info(f"Log created at {log_file}.")
  
