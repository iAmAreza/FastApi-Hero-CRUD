from sqlalchemy import Column, Integer, String
from app.database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    power = Column(String, index=True)