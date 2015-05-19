import sys

numbers = {1:'One',
           2:'Two',
           3:'Three',
           4:'Four',
           5:'Five',
           6:'Six',
           7:'Seven',
           8:'Eight',
           9:'Nine',
           10:'Ten',
           11:'Eleven',
           12:'Twelve',
           13:'Thirteen',
           14:'Fourteen',
           15:'Fifteen',
           16:'Sixteen',
           17:'Seventeen',
           18:'Eighteen',
           19:'Nineteen',
           20:'Twenty',
           30:'Thirty',
           40:'Forty',
           50:'Fifty',
           60:'Sixty',
           70:'Seventy',
           80:'Eighty',
           90:'Ninety',
           100:'Hundred',
           1000:'Thousand',
           1000000:'Million',
           1000000000:'Billion'
           }
           
def valOf(x):
    val = ''
    N = int(x)
    if N >= 1000000000:
        val = valOf(N/1000000000) + numbers[1000000000] + valOf(N%1000000000)
    elif N >= 1000000:
        val = valOf(N/1000000) + numbers[1000000] + valOf(N%1000000)
    elif N >= 1000:
        val = valOf(N/1000) + numbers[1000] + valOf(N%1000)
    elif N >= 100:
        val = valOf(N/100) + numbers[100] + valOf(N%100)
    elif N >= 20:
        val = numbers[(int(N/10)*10)] + valOf(N%10)
    elif N > 0:
        val = numbers[N]
    
    return val
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x = int(test.strip())
    print(valOf(x) + 'Dollars')
   

test_cases.close()
