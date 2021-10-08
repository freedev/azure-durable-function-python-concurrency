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

async def main(name: dict) -> str: 
    logging.info('#######  entering do_activity_async {str(name)}')
    logging.info('#######  entering do_activity_async')
    logging.info('#######  entering do_activity_async')
    logging.info('#######  entering do_activity_async')
    intensive_processing(10)
    logging.info('exiting do_activity_async ########')
    logging.info('exiting do_activity_async ########')
    logging.info('exiting do_activity_async ########')
    logging.info('exiting do_activity_async ########')
    return f'Hello {str(name)}!'
