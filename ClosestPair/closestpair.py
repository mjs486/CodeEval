import sys
test_cases = open(sys.argv[1], 'r')

numLines = int(test_cases.readline().strip())
while numLines != 0:
    points = []
    for i in range(numLines):
        [x,y] = test_cases.readline().strip().split(' ')
        points.append((float(x),float(y)))
    minDist = sys.maxsize
    for i in range(len(points)):
        for j in range(i,len(points)):
            if i != j:
                (x1,y1) = points[i]
                (x2,y2) = points[j]
                dist = ((x2 - x1)**2 + (y2 - y1)**2)**(.5)
                minDist = min(minDist,dist)
    print('{0:.4f}'.format(minDist))
    numLines = int(test_cases.readline().strip())
test_cases.close()
            
            
