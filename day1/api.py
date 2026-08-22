from fastapi import FastAPI
from system_utils import get_system_details

app=FastAPI(title="DevOps Utilities API")

@app.get("/hello")
def hello():
    return {"message": "Hello World, welcome to DevOps Utilities API"}

@app.get("/metrics")
def metrics():
    """
    This API shows the system information 
    like CPU, memory,disk,etc
    """
    return get_system_details()