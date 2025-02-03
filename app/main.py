from fastapi import FastAPI
from app.database import Base, engine
from app.routes import hero

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD with PostgreSQL")

# Include hero routes
app.include_router(hero.router, prefix="/heroes", tags=["Heroes"])
