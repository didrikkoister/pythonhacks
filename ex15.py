def max_in_list(values):
    if not (type(values) is list):
        #print "Not a list"
        return False
    max = values[0]
    for i in values[1:]:
        print "max is" + max
        if i > max:
            max = i
    return max
        
