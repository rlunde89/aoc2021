import numpy as np

with open('2\\2.input', 'r') as input_file:
    pos = [0,0]

    for maneuveur in [line.strip().split(" ") for line in input_file.readlines()]:
        if maneuveur[0] == "forward":
            pos[0] += int(maneuveur[1])
        else:
            pos[1] += int(maneuveur[1]) * {'up': -1, 'down': 1}[maneuveur[0]]
        
    print(pos[0] * pos[1])
