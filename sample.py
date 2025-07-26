def normalize(arr:list) -> list:
    arr_min = min(arr)
    diff = max(arr) - arr_min
    result = [((x - arr_min) / diff) for x in arr]
    return result

class TracePoint:
    def __init__(self, x:float, y:float, time_stamp:int) -> None:
        self.x = x
        self.y = y
        self.time_stamp = time_stamp
    
    def __iter__(self):
        return iter([self.x, self.y, self.time_stamp])

class Sample:
    """
    Samples consist of input_value and label. The input_value is a list of TracePoints.
    Each TracePoint has a value of x, y, and timestamp. 
    Each sample has an input length of 1215 TracePoints, and a label with the value of 0 or 1.
    """
    _ref_len = 1215 # all samples should have the same input length.
    
    def __init__(self, input_value:list[TracePoint], label_value:int) -> None:
        self.input_value = input_value
        self.label_value = label_value

        self.localize_coors()
        self.normalize_input()
        if len(input_value) < self._ref_len: self.pad_input()
        elif len(input_value) > self._ref_len: raise AssertionError(f"Sample length cannot be more than {self._ref_len}")
    
    def get_len(self) -> int:
        """returns the number of trace_points in this sample's input_value."""
        return len(self.input_value)

    def localize_coors(self) -> None:
        first_x_coor = self.input_value[0].x
        first_y_coor = self.input_value[0].y
        
        for i in range(self.get_len()):
            self.input_value[i].x -= first_x_coor
            self.input_value[i].y -= first_y_coor
    
    def normalize_input(self) -> None:
        tp_x = normalize([a.x for a in self.input_value])
        tp_y = normalize([a.y for a in self.input_value])
        tp_ts = normalize([a.time_stamp for a in self.input_value])
        
        for current_list in (tp_x, tp_y, tp_ts):
            assert min(current_list) == 0, f"min of normalized array is not 0"
            assert max(current_list) == 1, f"max of normalized array is not 1"
        
        for i in range(self.get_len()):
            self.input_value[i].x = tp_x[i]
            self.input_value[i].y = tp_y[i]
            self.input_value[i].time_stamp = tp_ts[i]
    
    def pad_input(self) -> None:
        diff = (self._ref_len - len(self.input_value))
        self.input_value.extend([TracePoint(0,0,0)] * diff)
        pass

    def __iter__(self):
        result = []
        for trace_point in self.input_value:
            result.append(list(trace_point))
        result.append([self.label_value, self.label_value, self.label_value])
        return iter(result)