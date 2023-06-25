from typing import Tuple

def convert_moves(round: Tuple[str, str]) -> Tuple[str, str]:
    move_map = {
        'A': 'R',
        'X': 'R',
        'B': 'P',
        'Y': 'P',
        'C': 'S',
        'Z': 'S',
    }

    return [move_map[round[0]], move_map[round[1]]]

def calc_rock_paper_scissors(opponent: str, player: str) -> str:
    if opponent == player:
        return 'draw'
    if opponent == 'R':
        return 'win' if player == 'P' else 'lose'
    if opponent == 'P':
        return 'win' if player == 'S' else 'lose'
    if opponent == 'S':
        return 'win' if player == 'R' else 'lose'

def calc_move_score(round: Tuple[str, str]) -> int:
    move_score_map = {
        'R': 1,
        'P': 2,
        'S': 3,
    }

    return move_score_map[round[1]]

def calc_game_score(round: Tuple[str, str]) -> int:
    game_score_map = {
        'lose': 0,
        'draw': 3,
        'win': 6,
    }

    result = calc_rock_paper_scissors(round[0], round[1])

    return game_score_map[result]