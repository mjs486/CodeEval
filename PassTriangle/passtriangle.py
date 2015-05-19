import sys
test_cases = open(sys.argv[1], 'r')

previous = [int(test_cases.readline())]

for test in test_cases:
    current = test.strip().split(' ')
    next = [0]*len(current)
    next[0] = int(current[0]) + previous[0]
    next[-1] = int(current[-1]) + previous[-1]
    for i in range(1,len(current)-1):
        next[i] = int(current[i]) + max(previous[i-1],previous[i])
    previous = next
test_cases.close()
print(max(previous))

