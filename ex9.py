from ex8 import reverse


def is_palindrome(str):
    print str
    newstring = ""
    for i in str:
        newstring = i + newstring 
    if newstring == str:
        return True
    else:
        return False

def palindrome2(str):
    newstring = reverse(str)
    if newstring == str:
        return True
    else:
        return False
