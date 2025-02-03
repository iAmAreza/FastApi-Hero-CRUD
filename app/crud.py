from sqlalchemy.orm import Session
from app.models import Hero
from app.schemas import HeroCreate

def create_hero(db: Session, hero: HeroCreate):
    new_hero = Hero(name=hero.name, power=hero.power)
    db.add(new_hero)
    db.commit()
    db.refresh(new_hero)
    return new_hero

def get_heroes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Hero).offset(skip).limit(limit).all()

def get_hero(db: Session, hero_id: int):
    return db.query(Hero).filter(Hero.id == hero_id).first()

def update_hero(db: Session, hero_id: int, hero_update: HeroCreate):
    hero = db.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        hero.name = hero_update.name
        hero.power = hero_update.power
        db.commit()
        db.refresh(hero)
    return hero

def delete_hero(db: Session, hero_id: int):
    hero = db.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        db.delete(hero)
        db.commit()
        return True
    return False
