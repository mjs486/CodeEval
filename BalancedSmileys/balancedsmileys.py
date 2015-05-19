import sys

def isBalanced(s):
    if not s:
        return True
    elif len(s) == 1 and (s.isalpha() or s == ' ' or s == ':'):
        return True
    else:
        maxParen = 0
        minParen = 0
        for i in range(len(s)):
            if s[i] == '(':
                maxParen += 1
                if i == 0 or s[i-1] != ':':
                    minParen += 1
            elif s[i] == ')':
                if i == 0 or s[i-1] != ':':
                    maxParen -= 1
                minParen = max(0,minParen-1)
        if maxParen >= 0 and minParen == 0:
            return True
        else:
            return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if isBalanced(test.strip()):
        print('YES')
    else:
        print('NO')

test_cases.close()
