import logging

import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        client = df.DurableOrchestrationClient(starter)
        instance_id = await client.start_new('orchestrator', None, {"activity": name, "do_something":'anything'})
        return func.HttpResponse(f"Trying to start activity: {name}. This HTTP triggered function executed successfully {instance_id}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
