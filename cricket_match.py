def test_win_or_lost(array):
    count = 0
    wicket = 0
    for val in array:
        try:
            count += int(val)
        except:
            if(val == "w"):
                wicket += 1
            else:
                for n in val:
                    try:
                        count += int(n)
                    except:
                        pass

    if(count >= 50 and wicket < 4):
        return "Win"
    else:
        return "Lose"
    
arr = []
for _ in range(5):
    try:
        arr += input().split(" ")
    except:
        pass
print(test_win_or_lost(arr))
