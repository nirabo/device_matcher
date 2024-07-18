# main.py
from fastapi import FastAPI
from routers import unstructured_assets_router, assets_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(assets_router.router)
app.include_router(unstructured_assets_router.router)
