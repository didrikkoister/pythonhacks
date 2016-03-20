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


