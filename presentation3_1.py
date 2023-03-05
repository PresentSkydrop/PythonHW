""" 3rd presentation — 26/02/2023

Write a program that assigns the name of 2 items to two variables. If the 2 values are equal, 
"The items are the same". Othervise, print "The items are different"
"""

a = "Mirror"
b = "Reflection"
c = "mirror"

print("Variables that are being compared: " + a + " and "+ b)
if(a==b):
    print("The items are the same \n")
else:
    print("The items are different\n")


print("Variables that are being compared: " + a + " and "+ c)
if(a==c):
    print("The items are the same \n")
else:
    print("The items are different\n")
    
    
#In case the items are the same, but the word has been entered w/ differential upper/lower case use 
print("Items that are being compared: " + a + " and "+ c)
if(a.lower()==c.lower()):
    print("The items are the same \n")
else:
    print("The items are different\n")