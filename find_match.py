def calculator(boy , girl):
    unique_boy = []
    unique_girl = []
    for letter in girl:
        if letter not in unique_girl:
            unique_girl.append(letter)
            
    for letter in boy:
        if letter not in unique_boy:
            unique_boy.append(letter)
    
    unique_girl.sort()
    unique_boy.sort()
    
    count_array_girl = []
    count_array_boy = []
    
    for k in unique_boy:
        count_array_boy.append(boy.count(k))
        
    for k in unique_girl:
        count_array_girl.append(girl.count(k))
    
    girl_accouring = ""
    boy_accouring = ""
    for n in range(3):
        index_g = count_array_girl.index(max(count_array_girl))
        index_b = count_array_boy.index(max(count_array_boy))
        
        girl_accouring += unique_girl[index_g]
        boy_accouring += unique_boy[index_b]
        
        count_array_girl[index_g] = 0
        count_array_boy[index_b] = 0
        
    print(boy_accouring)
    print(girl_accouring)
        
    if(girl_accouring == boy_accouring):
        return "Match"
    else:
        return "Not a Match"
    
print(calculator(list(input().lower()) , list(input().lower())))
