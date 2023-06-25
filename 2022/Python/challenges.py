from typing import Tuple

from helpers import read_input
from day_one_helpers import sum_groups, extract_groups_int
from day_two_helpers import convert_move, convert_moves, calc_move_score, calc_game_score, convert_win_lose_key, calc_player_move

def day_one_part_one():
    input = read_input('../day_one_input.txt')
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)

    return max(groups_sum)

def day_one_part_two():
    input = read_input('../day_one_input.txt')
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)
    groups_sorted = sorted(groups_sum)
    last_three = groups_sorted[-3:]

    return sum(last_three)


def day_two_part_one():
    input = read_input('../day_two_input.txt')
    rounds = [round.split(' ') for round in input.split('\n')]
    rounds = [convert_moves(round) for round in rounds]

    move_score = sum([calc_move_score(round) for round in rounds])
    game_score = sum([calc_game_score(round) for round in rounds])
    total_score = move_score + game_score

    return total_score

def day_two_part_two():
    input = read_input('../day_two_input.txt')
    rounds = [round.split(' ') for round in input.split('\n')]
    rounds = [[convert_move(round[0]), round[1]] for round in rounds]

    rounds_win_lose_converted = [convert_win_lose_key(round) for round in rounds]
    rounds_with_player_move = [calc_player_move(round) for round in rounds_win_lose_converted]

    move_score = sum([calc_move_score(round) for round in rounds_with_player_move])
    game_score = sum([calc_game_score(round) for round in rounds_with_player_move])
    total_score = move_score + game_score

    return total_score