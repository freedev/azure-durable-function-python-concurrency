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

def adding_delay(value):
   time.sleep(random.randint(5, 20) * 0.1)
   return value

async def main(name: dict) -> str: 
    logging.info("#######  entering do_activity")
    logging.info("#######  entering do_activity")
    logging.info("#######  entering do_activity")
    logging.info("#######  entering do_activity")
    time.sleep(10)
    logging.info("exiting do_activity ########")
    logging.info("exiting do_activity ########")
    logging.info("exiting do_activity ########")
    logging.info("exiting do_activity ########")
    return f"Hello {name}!"
