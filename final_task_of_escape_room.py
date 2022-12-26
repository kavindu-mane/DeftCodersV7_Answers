def palindrome(val):
    out = ""
    temp = 0
    oddLetter = ""
    if(len(val) % 2 == 0):
        for n in val:
            if(val.count(n) % 2 != 0):
                out = "NO"
                break
            else:
                out = "YES"
    else:
        for n in val:
            if(val.count(n) % 2 != 0):
                if(temp == 0 or oddLetter == n):
                    temp = 1
                    oddLetter = n
                    out = "YES"
                else:
                    out = "NO"
                    break
            else:
                out = "YES"
    return out

val = list(input())
val.sort()
print(palindrome(val))
