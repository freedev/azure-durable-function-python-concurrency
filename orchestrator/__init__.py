# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info("entering orchestrator")
    result1 = yield context.call_activity('do_activity', context.get_input())
    logging.info("exiting orchestrator")
    return [result1]

main = df.Orchestrator.create(orchestrator_function)