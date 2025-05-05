from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database
from datetime import datetime

router = APIRouter()

@router.get("/upcoming", response_model=list[schemas.MatchBase])
def get_upcoming(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Match).filter(models.Match.start_time > datetime.utcnow()).all()