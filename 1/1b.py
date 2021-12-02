import numpy as np
import pandas as pd

with open('1\\1.input', 'r') as input_file:
    depth_ctr, last_depth = 0, 1500  # should just be any large number. 
    
    frame = pd.DataFrame(columns=["meas"])
    frame["meas"] = [int(line) for line in input_file.readlines()]

    for depth in frame["meas"].rolling(3).sum().values:
        if depth > last_depth:
            depth_ctr += 1

        last_depth = depth

    print(depth_ctr)