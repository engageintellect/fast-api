from fastapi import FastAPI


root_msg = f'Welcome to Emerging Technologies'

info = {'info': 'Welcome to ET Info'};

release_notes = [
        {'date': '10-29-22', 'msg':'Playing with Fast API', 'link': 'et-dev.firstam.com'},
        {'date': '08-03-22', 'msg':'Weegle Prod v1.0 Release', 'link': 'et-dev.firstam.com'},
        {'date': '08-03-22', 'msg':'Testing', 'link': 'et-dev.firstam.com'},
        ]



#--------------------------
# API
#--------------------------
app = FastAPI()

@app.get("/")
async def root():
    return root_msg

@app.get("/info")
async def root():
    return info

@app.get("/release")
async def root():
    return release_notes
