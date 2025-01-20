import math
def v2_y(t, y):
    if t <= 0:
        return 0  
    return math.log(t) * y
