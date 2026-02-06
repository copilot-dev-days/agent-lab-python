from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict


class GameState(StrEnum):
    START = "start"
    PLAYING = "playing"
    BINGO = "bingo"


class BingoSquareData(BaseModel):
    """A single square on the bingo board."""

    model_config = ConfigDict(frozen=True)

    id: int
    text: str
    is_marked: bool = False
    is_free_space: bool = False


class BingoLine(BaseModel):
    """A winning line (row, column, or diagonal) on the board."""

    model_config = ConfigDict(frozen=True)

    type: Literal["row", "column", "diagonal"] = "row"
    index: int = 0
    squares: list[int] = []
