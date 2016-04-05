def is_member(val,mlist):
    if not (type(mlist) is list):
        print "not list"
        return False
    for i in mlist:
        print i
        if i == val:
            return True
    return False

def overlapping(alist,blist):
    if not (type(alist) is list) or not (type(blist) is list):
        print "not list"
        return False
    for i in alist:
        if is_member(i,blist):
            return True
    return False

    
    
