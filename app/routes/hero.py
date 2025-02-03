from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import create_hero, get_heroes, get_hero, update_hero, delete_hero
from app.schemas import HeroCreate, HeroResponse

router = APIRouter()

@router.post("/", response_model=HeroResponse)
def create(hero: HeroCreate, db: Session = Depends(get_db)):
    return create_hero(db, hero)

@router.get("/", response_model=list[HeroResponse])
def read(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_heroes(db, skip, limit)

@router.get("/{hero_id}", response_model=HeroResponse)
def read_one(hero_id: int, db: Session = Depends(get_db)):
    hero = get_hero(db, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@router.put("/{hero_id}", response_model=HeroResponse)
def update(hero_id: int, hero_update: HeroCreate, db: Session = Depends(get_db)):
    hero = update_hero(db, hero_id, hero_update)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@router.delete("/{hero_id}")
def delete(hero_id: int, db: Session = Depends(get_db)):
    if not delete_hero(db, hero_id):
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"message": "Hero deleted successfully"}
