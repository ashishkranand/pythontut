# using string concatenation
# me = "Ashish"
# al =5
# a="THis is %s%s"%(me,al)
# print(a)

# using format function

# me = "Ashish"
# al =5
# a = "This is {0} {1}"
# b = a.format(me,al)
# print(b)


# using fstring
import math
me = "Ashish"
al =5
a= f"This is {me} {al} {5*4} {math.cos(65)}"
print(a)

