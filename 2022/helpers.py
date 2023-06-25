from typing import List


def read_input() -> str:
    with open('./input.txt', 'r') as file:
        content = file.read()
    
    return content

def extract_groups_int(input: str) -> List[List[int]]:
    groups = input.split("\n\n")
    groups_int = [[int(line) for line in group.split('\n')] for group in groups]
    return groups_int

def sum_groups(input: List[List[int]]) -> List[int]:
    groups_summed = [sum(group) for group in input]

    return groups_summed