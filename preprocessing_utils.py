import numpy as np
from sample import *

def process_raw_data(raw_data:str):
    """
    takes raw data as input, and processes the data to be fed in to the nn.
    """
    trace_points:list[TracePoint] = []
    rds = raw_data.split(',') # rds: raw_data_split
    for i in range(0, len(rds), 3):
        trace_points.append(TracePoint(
            float(rds[i]), float(rds[i+1]), int(rds[i+2])
            ))
    
    sample = Sample(input_value=trace_points, label_value=-1)
    result = np.array([[[tp.x, tp.y, tp.time_stamp] for tp in sample.input_value]], dtype=np.float32)
    return result