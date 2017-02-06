import numpy as np

#test set of points
a = np.array([[-11.54337120056152, -7.660790920257568, 0],
[-11.54337120056152, -7.660790920257568, 16.0474910736084],
[3.485972881317139, -7.660790920257568, 0],
[3.485972881317139, -7.660790920257568, 16.0474910736084]])

#calculate the center

#calculate mean x
xPoints = a[:,0]
avgX = np.average(xPoints)
#calculate mean y
yPoints = a[:,1]
avgY = np.average(yPoints)
#calculate mean z
zPoints = a[:,2]
avgZ = np.average(zPoints)

centercheck = [avgX, avgY, avgZ]

i = 0
center = [0,0,0]
while (i < 3):
    points = a[:,i]
    center[i] = np.average(points)
    i += 1

print(centercheck)
print(center)

