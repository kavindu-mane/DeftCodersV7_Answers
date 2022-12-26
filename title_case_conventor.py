def conventor(array):
    non_conventors = ["and" , "but" , "or", "nor" , "for" , "with" , "to" , "at" , "of"]
    return_sentence = ""
    for word in array:
        if(word.lower() in non_conventors):
            return_sentence += word.lower() + " "
        else:
            return_sentence += (word[0].upper() + word[1:].lower()) + " "
    return return_sentence

print(conventor(input().split(" ")))
