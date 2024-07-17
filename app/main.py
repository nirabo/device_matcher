from fastapi import FastAPI
from routers.assets_router import assets_router

from database import Base, engine

app = FastAPI()
app.include_router(assets_router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)