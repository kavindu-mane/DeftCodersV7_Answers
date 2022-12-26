try:
    val = int(input())

    if(val > 0 and val < 1001):
        for k in range(1 , 13):
            print(str(val) + " x " + str(k).zfill(2) + " = " + str(val*k))
except:
    pass
