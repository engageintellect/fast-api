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
async def getInfo():
    return info

@app.get("/api/about")
async def getAbout():
    return about

@app.get("/api/releases")
async def getReleases():
    return release_notes

@app.get("/api/projects")
async def getProjects():
    return projects

@app.get("/api/products")
async def getProducts():
    return products
