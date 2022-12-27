def linear_or_not(house , arr):
    linears = []
    for k in arr:
        if(k[1] - k[0] == 1):
            linears.append(k[0])
            linears.append(k[1])
        else:
            break
    if(house in linears):
        return "NO"
    else:
        return "YES"

arr = []
try:
    house = int(input())
    loop_count = int(input())
    for _ in range(loop_count):
        arr.append(list(map(int , input().split(" "))))
    print(linear_or_not(house , arr))
except:
    pass
