from __future__ import annotations

import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.game_service import GameSession, get_session
from app.models import GameState

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Soc Ops - Social Bingo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

SESSION_COOKIE = "soc_ops_session"


def _session_from_request(
    request: Request,
) -> tuple[GameSession, Response]:
    """Get or create session, returning the session and a Response for cookies."""
    response = Response()
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        session_id = uuid.uuid4().hex
        response.set_cookie(SESSION_COOKIE, session_id, httponly=True, samesite="lax")
    return get_session(session_id), response


def _render(
    request: Request,
    response: Response,
    template: str,
    context: dict[str, Any],
) -> Response:
    """Render a template, copying any set-cookie headers from response."""
    content = templates.TemplateResponse(request, template, context)
    for key, value in response.headers.items():
        if key.lower() == "set-cookie":
            content.headers.append(key, value)
    return content


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Response:
    session, response = _session_from_request(request)
    return _render(
        request,
        response,
        "home.html",
        {"session": session, "GameState": GameState},
    )


@app.post("/start", response_class=HTMLResponse)
async def start_game(request: Request) -> Response:
    session, response = _session_from_request(request)
    session.start_game()
    return _render(
        request, response, "components/game_screen.html", {"session": session}
    )


@app.post("/toggle/{square_id}", response_class=HTMLResponse)
async def toggle_square(request: Request, square_id: int) -> Response:
    session, response = _session_from_request(request)
    session.handle_square_click(square_id)
    return _render(
        request, response, "components/game_screen.html", {"session": session}
    )


@app.post("/reset", response_class=HTMLResponse)
async def reset_game(request: Request) -> Response:
    session, response = _session_from_request(request)
    session.reset_game()
    return _render(
        request,
        response,
        "components/start_screen.html",
        {"session": session, "GameState": GameState},
    )


@app.post("/dismiss-modal", response_class=HTMLResponse)
async def dismiss_modal(request: Request) -> Response:
    session, response = _session_from_request(request)
    session.dismiss_modal()
    return _render(
        request, response, "components/game_screen.html", {"session": session}
    )


def run() -> None:
    """Entry point for the application."""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
