from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class MatchBase(BaseModel):
    id: int
    team_a: str
    team_b: str
    start_time: datetime
    team_a_score: int | None = None
    team_b_score: int | None = None
    is_finished: bool

    class Config:
        orm_mode = True

class PredictionCreate(BaseModel):
    match_id: int
    predicted_a: int
    predicted_b: int

class PredictionResponse(PredictionCreate):
    points: int
