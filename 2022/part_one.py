from extract_highest import extract_highest

with open('./input.txt', 'r') as file:
    content = file.read()
    answer = extract_highest(content)
    print(answer)
