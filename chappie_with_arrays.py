def func(a , b):
    if(a == 0):
        return b
    else:
        return func(b % a , a)

def calculation(line):
    line1 = line.copy()
    count = 0
    
    for k in range(len(line) - 1):
        for n in range(k+1 , len(line)):
            retVal = func(line1[k] , line1[n])
            if(retVal == 1):
                count += 1
                line1[k] = 0
                line1[n] = 0
            
    return count if count > 0 else -1

    
val = int(input())
for k in range(val):
    num =  int(input())
    line = list(map(int, input().split(" ")))
    print(calculation(line))
