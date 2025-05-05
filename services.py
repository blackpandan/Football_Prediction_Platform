from sqlalchemy.orm import Session
from . import models

def calculate_points(match: models.Match, prediction: models.Prediction) -> int:
    if match.team_a_score is None or match.team_b_score is None:
        return 0
    if prediction.predicted_a == match.team_a_score and prediction.predicted_b == match.team_b_score:
        return 3
    elif (prediction.predicted_a - prediction.predicted_b) == (match.team_a_score - match.team_b_score):
        return 1
    return 0

def process_match_results(match_id: int, db: Session):
    match = db.query(models.Match).filter(models.Match.id == match_id).first()
    if not match or not match.is_finished:
        return

    predictions = db.query(models.Prediction).filter(models.Prediction.match_id == match_id).all()
    for p in predictions:
        p.points = calculate_points(match, p)
        db.add(p)
    db.commit()