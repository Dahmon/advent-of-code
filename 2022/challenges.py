from helpers import sum_groups, read_input, extract_groups_int

def part_one():
    input = read_input()
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)

    return max(groups_sum)

def part_two():
    input = read_input()
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)
    groups_sorted = sorted(groups_sum)
    last_three = groups_sorted[-3:]

    return sum(last_three)
