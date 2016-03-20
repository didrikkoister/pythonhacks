def translate(str):
    newstr = " "
    conso = ["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    Uconso = ["Q","W","R","T","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    for i in str:
        if i in conso or i in Uconso:
            newstr = newstr + i + "o" + i
        else:
            newstr = newstr + i
    return newstr

def translater(str):
    conso = ["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    Uconso = ["Q","W","R","T","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    print str
    if len(str) < 1:
        return ""
    elif str[0] in conso or str[0] in Uconso:
        return  str[0] + "o" + str[0] + translater(str[1:])
    else:
        return str[0] + translater(str[1:])


