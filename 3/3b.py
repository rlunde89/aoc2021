import numpy as np
import pandas as pd

def return_sub_frame(bit_to_filter: int, input_frame: pd.DataFrame) -> float:
    out_frame = input_frame.copy()
    for col in out_frame:
        val_count = out_frame[col].value_counts()

        if bit_to_filter == 1:
            arg_val = val_count.idxmax() if (val_count.nunique() == 2) else bit_to_filter
        elif bit_to_filter == 0:
            arg_val = val_count.idxmin() if (val_count.nunique() == 2) else bit_to_filter

        out_frame = out_frame[out_frame[col] == arg_val]

        if len(out_frame) == 1:
            return int(''.join([str(val) for val in out_frame.mean().round(0).astype(int).values]), 2)



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
    
    oxygen = return_sub_frame(1, frame)
    o2 = return_sub_frame(0, frame)
    print(oxygen * o2)
