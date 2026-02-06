from __future__ import annotations

import random

from app.data import FREE_SPACE, QUESTIONS
from app.models import BingoLine, BingoSquareData

BOARD_SIZE = 5
CENTER_INDEX = 12  # 5x5 grid, center is index 12 (row 2, col 2)


def generate_board() -> list[BingoSquareData]:
    """Generate a new 5x5 bingo board."""
    shuffled = random.sample(QUESTIONS, 24)
    board: list[BingoSquareData] = []
    question_index = 0

    for i in range(25):
        if i == CENTER_INDEX:
            board.append(
                BingoSquareData(
                    id=i, text=FREE_SPACE, is_marked=True, is_free_space=True
                )
            )
        else:
            board.append(
                BingoSquareData(id=i, text=shuffled[question_index], is_marked=False)
            )
            question_index += 1

    return board


def toggle_square(
    board: list[BingoSquareData], square_id: int
) -> list[BingoSquareData]:
    """Toggle a square's marked state. Returns a new board list."""
    new_board: list[BingoSquareData] = []
    for square in board:
        if square.id == square_id and not square.is_free_space:
            new_board.append(
                BingoSquareData(
                    id=square.id,
                    text=square.text,
                    is_marked=not square.is_marked,
                    is_free_space=square.is_free_space,
                )
            )
        else:
            new_board.append(square)
    return new_board


def _get_winning_lines() -> list[BingoLine]:
    """Get all possible winning lines."""
    lines: list[BingoLine] = []

    # Rows
    for row in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for col in range(BOARD_SIZE)]
        lines.append(BingoLine(type="row", index=row, squares=squares))

    # Columns
    for col in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for row in range(BOARD_SIZE)]
        lines.append(BingoLine(type="column", index=col, squares=squares))

    # Diagonal (top-left to bottom-right)
    lines.append(BingoLine(type="diagonal", index=0, squares=[0, 6, 12, 18, 24]))

    # Diagonal (top-right to bottom-left)
    lines.append(BingoLine(type="diagonal", index=1, squares=[4, 8, 12, 16, 20]))

    return lines


def check_bingo(board: list[BingoSquareData]) -> BingoLine | None:
    """Check if there's a bingo and return the winning line."""
    for line in _get_winning_lines():
        if all(board[idx].is_marked for idx in line.squares):
            return line
    return None


def get_winning_square_ids(line: BingoLine | None) -> set[int]:
    """Get the square IDs that are part of a winning line."""
    if line is None:
        return set()
    return set(line.squares)
