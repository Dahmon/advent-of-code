from helpers import sum_groups, read_input, extract_groups_int

def part_one():
    input = read_input()
    groups_int = extract_groups_int(input)
    groups_sum = sum_groups(groups_int)

    return max(groups_sum)