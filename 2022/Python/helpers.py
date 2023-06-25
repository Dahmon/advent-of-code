def read_input(filename: str) -> str:
    with open(filename, 'r') as file:
        content = file.read()
    
    return content