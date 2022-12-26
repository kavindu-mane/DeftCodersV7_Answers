def calc(line):
    out = ""
    for k in range(1 ,6):
        out += str(line.count(k))
        if(k != 5):
            out += " "
    return out

val = int(input())
print(calc(list(map(int , input().split(" ")))))

# Test case 3 (sample test case 1) has wrong output
