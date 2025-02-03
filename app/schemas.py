from pydantic import BaseModel

class HeroBase(BaseModel):
    name: str
    power: str

class HeroCreate(HeroBase):
    pass

class HeroResponse(HeroBase):
    id: int

    class Config:
        orm_mode = True
