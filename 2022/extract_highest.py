def extract_highest(input: str):
    groups = input.split("\n\n")
    groups_int = [[int(line) for line in group.split('\n')] for group in groups]
    groups_summed = [sum(group) for group in groups_int]

    return max(groups_summed)