from fastapi import FastAPI
from data import *

#--------------------------
# API
#--------------------------

app = FastAPI()


class Record:
    def __init__ (self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    def getRecord(self):
        return self


x = Record('dark side of the moon', 'pink floyd', 'rock')




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

@app.get("/api/testing")
async def getTesting():
    return x.getRecord()
