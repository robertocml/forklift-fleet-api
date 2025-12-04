from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import forklift

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(forklift.router)