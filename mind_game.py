def choose_winner(h_arr, p_arr):
    h_count = sum(h_arr)
    p_count = sum(p_arr)
    
    if(h_count > p_count):
        return "HANSANA"
    else:
        return "PRASAD"
try:    
    loop_count = int(input())
    for _ in range(loop_count):
        length = int(input())
        h_arr = list(map(int , input().split(" ")))
        p_arr = list(map(int , input().split(" ")))
        print(choose_winner(h_arr, p_arr))
except:
    pass
