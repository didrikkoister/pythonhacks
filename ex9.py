from ex8 import reverse


def is_palindrome2(str):
    str1 = str.replace(" ","").lower()
    print str1
    newstring = ""
    for i in str1:
        newstring = i + newstring 
    if newstring == str1:
        return True
    else:
        return False
def cleanstring(str):
    cleanout = " ,;:$%"
    for i in cleanout:
        str = str.replace(i,"")
    return str


def is_palindrome(str):
    str1 = cleanstring(str).lower()
    newstring = reverse(str1)
    if newstring == str1:
        return True
    else:
        return False
