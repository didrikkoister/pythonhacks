print("Testing palindromes")

def test_pali(a,correct):
    ans = is_palindrom(a)
    if ans == correct:
        print "Correct: " + a
    else:
        print "Incorrect: " + a


a="A but tuba"
test_pali(a)
b="A car, a man, a maraca"
test_pali(b)

c="Amen icy cinema"
test_pali(c)

