from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.game_service import get_session
from app.models import GameState

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Soc Ops - Social Bingo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

SESSION_COOKIE = "soc_ops_session"


def _get_session_id(request: Request, response: Response) -> str:
    """Get or create a session ID from cookies."""
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        session_id = uuid.uuid4().hex
        response.set_cookie(SESSION_COOKIE, session_id, httponly=True, samesite="lax")
    return session_id


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Response:
    response = Response()
    session_id = _get_session_id(request, response)
    session = get_session(session_id)

    content = templates.TemplateResponse(
        request,
        "home.html",
        {"session": session, "GameState": GameState},
    )
    # Copy cookies from our response to the template response
    for key, morsel in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, morsel)
    return content


@app.post("/start", response_class=HTMLResponse)
async def start_game(request: Request) -> Response:
    response = Response()
    session_id = _get_session_id(request, response)
    session = get_session(session_id)
    session.start_game()

    content = templates.TemplateResponse(
        request,
        "components/game_screen.html",
        {"session": session},
    )
    for key, morsel in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, morsel)
    return content


@app.post("/toggle/{square_id}", response_class=HTMLResponse)
async def toggle_square(request: Request, square_id: int) -> Response:
    response = Response()
    session_id = _get_session_id(request, response)
    session = get_session(session_id)
    session.handle_square_click(square_id)

    content = templates.TemplateResponse(
        request,
        "components/game_screen.html",
        {"session": session},
    )
    for key, morsel in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, morsel)
    return content


@app.post("/reset", response_class=HTMLResponse)
async def reset_game(request: Request) -> Response:
    response = Response()
    session_id = _get_session_id(request, response)
    session = get_session(session_id)
    session.reset_game()

    content = templates.TemplateResponse(
        request,
        "components/start_screen.html",
        {"session": session, "GameState": GameState},
    )
    for key, morsel in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, morsel)
    return content


@app.post("/dismiss-modal", response_class=HTMLResponse)
async def dismiss_modal(request: Request) -> Response:
    response = Response()
    session_id = _get_session_id(request, response)
    session = get_session(session_id)
    session.dismiss_modal()

    content = templates.TemplateResponse(
        request,
        "components/game_screen.html",
        {"session": session},
    )
    for key, morsel in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, morsel)
    return content


def run() -> None:
    """Entry point for the application."""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
