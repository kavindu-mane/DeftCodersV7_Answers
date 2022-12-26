def allow_or_notallow(userVal , line):
    domains = ["au" , "de" , "fr" ,"hk" , "id" ,"in" ,"jp" ,"lk","mm" ,"nz" ,"ru","uk" ,"us","vn"]
    topDomains = ["com" ,"dev","crew"]

    if(len(userVal[0]) < 4 or len(userVal[0]) > 10 or len(userVal) != 2):
         return "BLOCKED"
    else:
        for n in (userVal[0]):
            if(ord(n) < 48 or (ord(n) > 57 and ord(n) < 65) or (ord(n) > 90 and ord(n) < 97) or ord(n) > 122):
                return "BLOCKED"
        if(line[0] == "nanolabs" and line[1] in topDomains):
            if((len(line) == 3 and line[2] in domains) or (len(line) == 2 and line[1] == "com")):
                return "ALLOWED"
            else:
                return "BLOCKED"
        else:
            return "BLOCKED"

val =  int(input())
for _ in range(val):
    userVal = input().split("@")
    line = (userVal[1]).split(".")
    print(allow_or_notallow(userVal , line))
