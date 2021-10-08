import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    resp = {'status': 'OK'}

    if resp.get('status') == 'OK':
            return func.HttpResponse(
                    json.dumps(resp),
                    mimetype='application/json',
                    status_code=200
            )

    return func.HttpResponse(
            json.dumps({'msg': 'health test failed'}),
            mimetype='application/json',
            status_code=500
    )