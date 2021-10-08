# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

from lib import async_executor, intensive_processing

async def main(name: dict) -> str: 
    logging.info('#######  entering do_activity_async_wrapped {str(name)}')
    logging.info('#######  entering do_activity_async_wrapped')
    logging.info('#######  entering do_activity_async_wrapped')
    logging.info('#######  entering do_activity_async_wrapped')
    l = lambda: intensive_processing(10)
    await async_executor(l)
    logging.info('exiting do_activity_async_wrapped ########')
    logging.info('exiting do_activity_async_wrapped ########')
    logging.info('exiting do_activity_async_wrapped ########')
    logging.info('exiting do_activity_async_wrapped ########')
    return f'Hello {str(name)}!'
