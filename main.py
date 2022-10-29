from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/info")
async def root():
    return {"message": "This is some info"}

@app.get("/release")
async def root():
    return {
            "date": "10-28-22",
            "title": "This is a title",
            "message": "This is a message",
            "link": "https://google.com",
            }

