from fastapi import FastAPI
from data import *


#--------------------------
# API
#--------------------------
app = FastAPI()

@app.get("/")
async def root():
    return root_msg

@app.get("/api/info")
async def root():
    return info

@app.get("/api/release")
async def root():
    return release_notes

@app.get("/api/projects")
async def root():
    return projects

@app.get("/api/products")
async def root():
    return products

