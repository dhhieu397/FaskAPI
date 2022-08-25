from fastapi import FastAPI, UploadFile, File
from typing import List
import shutil
app = FastAPI()
@app.post("/")
async def root(file: UploadFile = File(...)): #param: file; type: UploadFile; import file from fastapi
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}

#load many file:

@app.post("/img")
async def root(files: List[UploadFile] = File(...)): #param: file; type: UploadFile; import file from fastapi
    for img in files:

        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)
    return {"file_name": img.filename}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

