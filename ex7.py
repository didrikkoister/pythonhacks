def sum(numbers):
    zsum = 0
    for i in numbers:
        #print "zsum = " +  str(zsum)
        #print "i = " + str(i)
        zsum = i + zsum
    return zsum

def sumr(numbers):
    if len(numbers) <= 1:
        return numbers[0]
    else:
        return numbers[0] + sumr(numbers[1:])

def multiply(numbers):
    product = 1
    for i in numbers:
        print "product is " + str(product)
        print "i is " + str(i)
        product = i * product
    return product

def multiplyr(numbers):
    print numbers
    if len(numbers) <= 1:
        return numbers[0]
    else:
        return numbers[0] * multiplyr(numbers[1:])


#testcall

print str(multiplyr([1,2,3,4]))

sumr([1,2,3,4])


