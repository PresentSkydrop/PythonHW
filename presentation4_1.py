#Presentation 4 - Task 1 —01/03/2023
# Write a function to find the Max of three numbers

def Max(a,b,c):
    if a < b:
        if c < b:
            print("The Max number of the provided three is: ", b)
        else:
            print("The Max number of the provided three is: ", c)
    else:
        if a > c:
            print("The Max number of the provided three is: ", a)
        else:
            print("The Max number of the provided three is: ", c)

# User inputs values             
a = input("Please enter a number: ")
b = input("Please enter another number: ")
c = input("Please enter another number: ")

print("You have entered such numbers: " )
print(a, " ", b, " ", c)

#function Max is called 
Max(a, c, b)
    