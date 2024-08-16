from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import predict
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

# Mount the static files (like CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="app/templates")

# Include the router from predict.py
app.include_router(predict.router)

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})



# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi import Request

# app = FastAPI()

# # Mount the static directory
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# # Set up templates
# templates = Jinja2Templates(directory="app/templates")

# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/prediction")
# def read_prediction(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
