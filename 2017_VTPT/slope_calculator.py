# sorting 

import numpy as np
import math as m

a = np.array([[-1, 1, 0],
[1, 1, 0],
[1, -1, 0],
[-1, -1, 0]])

center = [0,0,0]


#find 3D slope

#find run
lastPoint = len (a)
index = 0
run = [0,0,0,0]
for point in range (0, lastPoint):
    xDif = center[0] - point[0]
    absXDif = abs(xDif)
    yDif = center[1] - point[1]
    absYDif = abs(yDif)
    run[point] = m.sqrt(absXDif*absXDif +absYDif*absYDif)
    