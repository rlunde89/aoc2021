import numpy as np

with open('1\\1.input', 'r') as input_file:
    last_depth = 1500
    depth_ctr = 0
    
    for depth in [int(line) for line in input_file.readlines()]:
        if depth > last_depth:
            depth_ctr += 1
        last_depth = depth
    print(depth_ctr)