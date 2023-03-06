#Presentation 4 - Task 2 —01/03/2023
#Python program that reverses a string 


def reverse(string): #function where the string is printed in reverse in seperate characters
    lenght = len(string)
    lenght = lenght-1
    while(lenght != 0):
        print(string[lenght])
        lenght-=1
        
def reverseString(string): # function that creates a reverse string 
    lenght = len(string)
    print(len(string))
    lenght = int(lenght-1)
    x = int(lenght)
    revstr = string[lenght]
    while(lenght > -1):
        if lenght != x:
            revstr = revstr + string[lenght]
        lenght-=1
    print(revstr)
   #return string # delete the "#" in order to return a value from this function
      

sample = "1234abcd"
print(sample)
#reverse(sample)
reverseString(sample)
#sample = reverseString(sample) #this is to be unlocked if we wish to set the strings value to the reverse string and if the return is set in action


    