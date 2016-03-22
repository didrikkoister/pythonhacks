def reverse(str):
    print str
    newstring = ""
    for i in str:
        newstring = i + newstring
    return newstring


def reverser(str):
    print str
    if len(str) < 1:
        return str
    else:
        return reverser(str[1:]) + str[0]
