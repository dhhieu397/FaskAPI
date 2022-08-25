from fastapi import FastAPI, Body, Request, File, UploadFile, Form
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException
# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )


app =FastAPI()

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)
#

list_of_usernames =list()
templates = Jinja2Templates(directory='templates')

class NameValues(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float

@app.get("/home/{user_name}", response_class=HTMLResponse)
async def write_home(request: Request, user_name: str):
    return templates.TemplateResponse(('home.html'),{"request":request,"username":user_name})

@app.post("/submitform")
async def handle_form(assignment: str = Form(...), assignment_file: UploadFile = File(...)):
    print(assignment)
    print(assignment_file.filename)
    content_assignment = await assignment_file.read()
    print(content_assignment)
    return {'file':assignment_file.filename, 'content':content_assignment}

@app.get("/postData")
async def post_data(name_value: NameValues, spousal_status: str = Body(...)):
    print(name_value)
    return {
        "name":name_value.name,
        "spousal_status":spousal_status
    }