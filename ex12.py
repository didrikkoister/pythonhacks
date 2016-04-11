def generate_n_chars(n,c):
    if not (type(n) is int):
        print "not int"
        return False
    if not (type(c) is str):
        print "not a string"
        return False
    y = 0
    s = ""
    while n > y:
        y = y + 1
        s = s + c
    print s


#13

def histogram(values):
    if not (type(values) is list):
        print "not a list"
        return False
    for i in values:
        if type(i) is int:
            generate_n_chars(i,"*")
        else:
            print "#"

