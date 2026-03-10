a=5.08  #the estimated population of Scotland in 2004
b=5.33  #the estimated population of Scotland in 2014
c=5.55  #the estimated population of Scotland in 2024

d=b-a   #the change in population between 2004 and 2014
e=c-b   #the change in population between 2014 and 2024

print("the change in population between 2004 and 2014 is",d)
print("the change in population between 2014 and 2024 is",e)

#d is larger than e, population	growth is decelerating in Scotland.

X = True
Y = False
W = X or Y
print("X or Y =", W)

#the truth table for W
# X      | Y      | W (X or Y)
# ----------------------------
# True   | True   | True
# True   | False  | True
# False  | True   | True
# False  | False  | False