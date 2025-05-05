from fastapi import HTTPException

def validate_prediction_time(match, now):
    if match.start_time <= now:
        raise HTTPException(status_code=400, detail="Cannot predict after match start")


def check_duplicate_prediction(db, user_id, match_id):
    existing = db.query(models.Prediction).filter_by(user_id=user_id, match_id=match_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Prediction already exists")