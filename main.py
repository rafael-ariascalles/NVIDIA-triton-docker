from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests
import os
#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/

app = FastAPI("Triton Health Check")

@app.get("/")
#Call your get function for a health Check
async def healthcheck():
    #to receive both (face-bokeh and face-emotion)
    service_boke = requests.get(os.getenv('SERVICE_BOKE'))
    service_emotion = requests.get(os.getenv('SERVICE_EMOTION'))

    return "OK"
