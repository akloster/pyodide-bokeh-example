from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "rt") as f:
        return f.read()

app.mount("/pyodide", StaticFiles(directory="pyodide"), name="pyodide")
app.mount("/static", StaticFiles(directory="static"), name="static")

