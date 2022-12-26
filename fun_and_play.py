iter  = 2
lines = []
try:
    val = int(input())
    if(val<1):
        print("Incorrect Input")
    else:
        for k in range(val):
            line = [1]
            for n in range(k):
                if(n == (k -1)):
                    line.append(line[-1] + 1)
                else:
                    line.append(lines[-1][n] + lines[-1][n+1])
            lines.append(line)
            
        for k in lines:
            length = 0
            for n in k:
                length += 1
                if(length != len(k)):
                    print(n , end= ", ")
                else:
                    print(n)
    
except:
    print("Incorrect Input")
