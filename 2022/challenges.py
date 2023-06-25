from helpers import read_input
from day_one_helpers import sum_groups, extract_groups_int

def day_one_part_one():
    input = read_input('day_one_input.txt')
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)

    return max(groups_sum)

def day_one_part_two():
    input = read_input('day_one_input.txt')
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)
    groups_sorted = sorted(groups_sum)
    last_three = groups_sorted[-3:]

    return sum(last_three)
