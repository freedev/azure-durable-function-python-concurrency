# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import time
import random

from lib import intensive_processing

def main(name: dict) -> str: 
    logging.info("#######  entering do_activity_sync")
    logging.info("#######  entering do_activity_sync")
    logging.info("#######  entering do_activity_sync")
    logging.info("#######  entering do_activity_sync")
    intensive_processing(10)
    logging.info("exiting do_activity_sync ########")
    logging.info("exiting do_activity_sync ########")
    logging.info("exiting do_activity_sync ########")
    logging.info("exiting do_activity_sync ########")
    return f"Hello {str(name)}!"
