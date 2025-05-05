from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/updates")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Connected to live updates")
    while True:
        await websocket.send_text("Update from server")