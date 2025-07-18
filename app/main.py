from fastapi import FastAPI
from app.routes import analysis

app = FastAPI()
app.include_router(analysis.router, prefix="/resume")
