# Provides log messages in both files and console

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  # log message string

logging_dir = "logs"  # directory where log messages are stored
log_filepath = os.path.join(logging_dir, "running_logs.log") # file where log messages are stored
os.makedirs(logging_dir, exist_ok=True) # create the log directory 

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # log messages in file
        logging.StreamHandler(sys.stdout) # log messages in console
    ]
)

logger = logging.getLogger("mlProjectLogger")