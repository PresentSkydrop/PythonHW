"""  3rd presentation — 26/02/2023
Write a program to ask for name and age.
When both values have been entered, check if the person is the right age. A person must le an adult.

If they are, welcome them.
Otherwise, print a polite rejection text.
"""
#This example assumes that the user will enter their age using numbers not letters
age = int(input("Please state your age (please use numbers):"))
name = input("Plese enter your name: ")
if age<18:
    reject = "{0}, unfurtunately we are unable to process your request as you do not match our age requirements."
    print(reject.format(name))
else:
    print("Welcome "+ name + "!")


    