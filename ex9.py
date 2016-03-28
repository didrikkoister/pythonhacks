from ex8 import reverse



#removes unwanted signs and spaces 
def cleanstring(str):
    cleanout = " ,;:$%"
    for i in cleanout:
        str = str.replace(i,"")
        #print str
    return str


def mycleanstring(str):
    newstr = ""
    for i in str:
        if i == " ":
            newstr = newstr
        elif i == ",":
            newstr = newstr
        elif i == ";":
            newstr = newstr
        elif i == ":":
            newstr = newstr
        elif i == "$":
            newstr = newstr
        elif i == "%":
            newstr = newstr
        else:
            newstr = newstr +i
       # print newstr
    return newstr

def is_palindrome2(str):
    str1 = mycleanstring(str).lower()
    print str1
    newstring = ""
    for i in str1:
        newstring = i + newstring 
    if newstring == str1:
        return True
    else:
        return False



def is_palindrome(str):
    str1 = cleanstring(str).lower()
    newstring = reverse(str1)
    if newstring == str1:
        return True
    else:
        return False
