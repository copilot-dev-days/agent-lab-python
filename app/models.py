from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class GameState(str, Enum):
    START = "start"
    PLAYING = "playing"
    BINGO = "bingo"


@dataclass
class BingoSquareData:
    id: int
    text: str
    is_marked: bool = False
    is_free_space: bool = False


@dataclass
class BingoLine:
    type: str = ""  # "row", "column", or "diagonal"
    index: int = 0
    squares: list[int] = field(default_factory=list)
