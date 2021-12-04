import numpy as np
import pandas as pd

with open('3\\3.input', 'r') as input_file:
    j = 0
    for reading in [line.strip() for line in input_file.readlines()]:
        input = [int(val) for val in reading]
        try:
            frame.loc[j, :] = input
        except:
            frame = pd.DataFrame(columns = range(len(input)))
            frame.loc[0, :] = input
        
        j+=1

    gamma = ''.join([str(val) for val in frame.mean().round(0).astype(int).values])
    epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
    print(int(gamma,2) * int(epsilon, 2))
    print(epsilon)
