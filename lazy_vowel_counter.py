def counter(sentence):
    vowels = ["a", "e" ,"i" ,"o" , "u"]
    count = 0
    for letter in sentence:
        if(letter.lower() in vowels):
            count += 1
    return count

print(counter(input()))
