from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

@router.get("/")
def get_leaderboard(db: Session = Depends(database.SessionLocal)):
    results = db.query(models.Prediction.user_id, models.User.username, 
                       models.Prediction.points).join(models.User).all()
    scores = {}
    for uid, username, points in results:
        scores[username] = scores.get(username, 0) + (points or 0)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)