from fastapi import FastAPI, Request, HTTPException, Depends
import boto3
import json
#from config import Settings, get_settings

app = FastAPI()

#def get_sqs_client(settings: Settings = Depends(get_settings)):
#    return boto3.client(
#        'sqs',
#        aws_access_key_id=settings.aws_access_key_id,
#        aws_secret_access_key=settings.aws_secret_access_key,
#        region_name=settings.aws_region
#    )

#@app.post("/webhook")
#async def webhook(
#    request: Request,
#    settings: Settings = Depends(get_settings),
#    sqs_client: boto3.client = Depends(get_sqs_client)
#):
#    try:
#        # Recebe o payload do WhatsApp
#        payload = await request.json()
#        
#        # Envia a mensagem para o SQS
#        response = sqs_client.send_message(
#            QueueUrl=settings.sqs_queue_url,
#            MessageBody=json.dumps(payload)
#        )
#        
#        print(f"Mensagem enviada para SQS. MessageId: {response['MessageId']}")
#        
#        return {"status": "success"}
#    
#    except Exception as e:
#        print(f"Erro: {str(e)}")
#        return {"status": "success"}
#
#@app.get("/webhook")
#async def verify_webhook(
#    request: Request,
#    settings: Settings = Depends(get_settings)
#):
#    try:
#        params = dict(request.query_params)
#        
#        if params.get('hub.mode') == 'subscribe' and params.get('hub.verify_token'):
#            if params.get('hub.verify_token') == settings.whatsapp_verify_token:
#                return int(params.get('hub.challenge'))
#            raise HTTPException(status_code=403, detail="Invalid verify token")
#        
#        raise HTTPException(status_code=400, detail="Invalid request")
#    
#    except HTTPException as he:
#        raise he
#    except Exception as e:
#        print(f"Erro na verificação: {str(e)}")
#        raise HTTPException(status_code=400, detail="Invalid request")
#

@app.get("/health")
async def health_check():
    return {"status": "healthy"}