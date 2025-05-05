from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from datetime import datetime

router = APIRouter()

@router.post("/submit", response_model=schemas.PredictionResponse)
def submit_prediction(pred: schemas.PredictionCreate, user_id: int = 1, db: Session = Depends(database.SessionLocal)):
    match = db.query(models.Match).filter(models.Match.id == pred.match_id).first()
    if not match or match.start_time <= datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired match")

    existing = db.query(models.Prediction).filter_by(user_id=user_id, match_id=pred.match_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already predicted")

    prediction = models.Prediction(user_id=user_id, match_id=pred.match_id,
                                   predicted_a=pred.predicted_a, predicted_b=pred.predicted_b)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction