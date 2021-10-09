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
    logging.info(f'#######  entering {name["activity"]}')
    logging.info(f'#######  entering {name["activity"]}')
    logging.info(f'#######  entering {name["activity"]}')
    logging.info(f'#######  entering {name["activity"]}')
    resp = intensive_processing('input')
    logging.info(f'#######  leaving {resp}')
    logging.info(f'#######  leaving {resp}')
    logging.info(f'#######  leaving {resp}')
    logging.info(f'#######  leaving {resp}')
    return f'Hello {str(name)}!'
