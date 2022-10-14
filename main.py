from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests
import os
#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/

app = FastAPI(title="Triton Health Check")

@app.get("/")
#Call your get function for a health Check
async def healthcheck():
    #to receive both (face-bokeh and face-emotion)
    service_boke = requests.get(os.getenv('SERVICE_BOKE'))
    service_emotion = requests.get(os.getenv('SERVICE_EMOTION'))
    
    return {"boke":service_boke.json(),"emotion":service_emotion.json()}
