from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    team_a = Column(String)
    team_b = Column(String)
    start_time = Column(DateTime)
    team_a_score = Column(Integer, nullable=True)
    team_b_score = Column(Integer, nullable=True)
    is_finished = Column(Boolean, default=False)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    match_id = Column(Integer, ForeignKey("matches.id"))
    predicted_a = Column(Integer)
    predicted_b = Column(Integer)
    points = Column(Integer, default=0)