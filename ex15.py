def max_in_list(values):
    if not (type(values) is list) or len(values) < 1:
        print "Not a list"
        return False
    max = values[0]
    for i in values[1:]:
        #print "max is" +str(max)
        if i > max:
            max = i
    return max
        


def mmax_in_list(values):
    if len(values) < 1:
        print "empty"
        return 0
    if len(values) == 1:
        return values[0]
    first = values[0]
    new = mmax_in_list(values[1:])
    if first > new:
        return first
    else:
        return new
