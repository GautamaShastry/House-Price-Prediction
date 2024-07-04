import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_dir = "logs"
log_filepath = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

logging.basicConfig(
    filename=log_filepath, 
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

