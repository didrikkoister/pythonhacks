from ex9 import *



def test_pali(a,correct):
    print("Testing is_palindrome")
    ans = is_palindrome(a)
    if ans == correct:
        print "Correct: " + a
    else:
        print "Incorrect: " + a


a="A but tuba"
test_pali(a,True)
b="A car, a man, a maraca"
test_pali(b,True)
c="Amen icy cinema"
test_pali(c,True)
test_pali("radar",True)
test_pali("didrik",False)

def test_pali2(a,correct):
    print("Testing is_palindrome2")
    ans = is_palindrome2(a)
    if ans == correct:
        print "Correct: " + a
    else:
        print "Incorrect: " + a



a="A but tuba"
test_pali2(a,True)
b="A car, a man, a maraca"
test_pali2(b,True)
c="Amen icy cinema"
test_pali2(c,True)
test_pali2("radar",True)
test_pali2("didrik",False)
