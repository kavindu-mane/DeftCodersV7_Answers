line = input()
code = input()
word = ""
index = 0

if(len(line) > 3 and len(line) < 100 and len(code) > 2 and len(code)< 10):
    for k in line:
        word += chr(65 + (ord(k) - ord(code[index % len(code)])) % 26)
        index += 1
    print(word)
