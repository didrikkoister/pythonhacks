def strlengths(lists):
    lengths = []
    for i in lists:
        lengths.append(len(i))
    return lengths

def strlengthsrec(lists):
    if len(lists) < 1:
        return []
    else:
        #calculate length of 1st element, create new list from element
        #recursive call to get the lengths of the rest of the elements
        #merge elements into new list, return merged list
        
        calc = [len(lists[0])]
        new = strlengthsrec(lists[1:])
        return calc + new
