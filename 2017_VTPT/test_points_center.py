#unit tests for points_center.py
a = np.array([[-1, 1, 0],
[1, 1, 0],
[1, -1, 0],
[-1, -1, 0]])

a = np.array([[0,-1, 1],
[0, 1, 1],
[0, 1, -1],
[0, -1, -1]])

i = 0
center = [0,0,0]
while (i < 3):
    points = a[:,i]
    center[i] = np.average(points)
    i += 1
    
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

print(centercheck)

print(center)