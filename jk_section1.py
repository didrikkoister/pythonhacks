#nytt program
def max(a,b):
  if (a > b) :
      return a
  else :
      return b


print "max of numbers"
print max(3,4)
print max(3,5)

#assignment 3

def max_of_three(a,b,c):
  if (a > b and a >  c) :
    return a
  elif (b > c):
    return b
  else:
    return c
    
print "Correct answer is 3"
print max_of_three(3,2,1)
print "Correct answer is 7"
print max_of_three(7,1,6)
print "Correct answer is 25"
print max_of_three(4,9,25)

#4

def length(str):
  j=0
  for i in str:
    j=j+1
  return j



str1 = "hej didrik"
print "length of " + str1 + " is " + str(length(str1))
str1 = "hej"
print "length of " + str1 + " is " + str(length(str1))
str1 = "hejsan didrik"
print "length of " + str1 + " is " + str(length(str1))

def lengthr(str):
  if (length(str) == 1):
    return 1
  else:
    return lengthr(str[1:]) + 1
  
str1 = "hej didrik"
print "lengthr of " + str1 + " is " + str(lengthr(str1))
str1 = "hej"
print "lengthr of " + str1 + " is " + str(lengthr(str1))
str1 = "hejsan didrik"
print "lengthr of " + str1 + " is " + str(lengthr(str1))

#5
from sets import Set

def isvowels(char):
  vowels = Set(['o','u','e','a','i','y'])
  if char in vowels:
    print "True"
  else:
    print "false"

print "r is vowel "
isvowels("r")
print "u is vowel "
isvowels("u")


def isvowell(char):
  v = "oueaiy"
  for i in v:
    if char == i:
      print "True"
      return
  print "false"

print "r is vowel "
isvowell("r")
print "u is vowel "
isvowell("u")


  
