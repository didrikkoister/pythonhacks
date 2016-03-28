from ex9 import *

print("Testing palindromes")

def test_pali(a,correct):
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

