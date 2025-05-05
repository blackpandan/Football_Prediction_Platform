from fastapi import FastAPI
from routes import auth, matches, predictions, leaderboard, websocket

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(matches.router, prefix="/matches")
app.include_router(predictions.router, prefix="/predictions")
app.include_router(leaderboard.router, prefix="/leaderboard")
app.include_router(websocket.router, prefix="/ws")
