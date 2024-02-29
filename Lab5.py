# Lab5
# Author: Laci Trull

"""_summary_
This lab is designed to get you familiar with Python Functions, parameters, return values, Type Hinting, and Docstrings.

Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.
"""
# 1. Write a function called number_squared(num) that takes a number as a parameter and prints out the number squared. Include Type Hinting and a Docstring.
def number_squared(num: int) -> int:
    """Input number and return the number squared
    Args:
    num (int): the number to square
    Returns:
    int: the number squared
    """
    return num**2

print(number_squared(5))
# 2. Write a function called string_counter(str) that take a string as a parameter and tell you how many letters are in the string. Include Type Hinting and a Docstring.
def string_counter(str: str) -> int:
    """Input a string and return the number of letters in the string
    Args:
    str (str): the string to count
    Returns:
    int: the number of letters in the string
    """
    return len(str)
# 4. Write a function called number_adder(num1, num2) that takes two numbers as parameters and returns the sum of the two numbers. Include Type Hinting and a Docstring.
def number_adder(num1: int, num2: int) -> int:
    """takes in two numbers and returns the sum of the two numbers
    Args:
    num1 (int): number 1
    num2 (int): number 2
    Returns:
    int: the sum of the two numbers"""
    return num1 + num2
# 5. Write a function called jacket_checker(temp, raining) that takes in a temperature (int) and whether it is raining (bool) as parameters and prints out whether you should wear a jacket or not. If the temperature is above 60 Degrees and it is not raining you should return not to wear a jaket. Return a String "Wear a Jacket" or "Do not wear a Jacket".  Include Type Hinting and a Docstring.
def jacket_checker(temp: int, raining: bool) -> str:
    """Jacket Checker: Will take in an int and boot and return whether you should wear a jacket or not
   
    Args:
    temp (int): the temperature outside
    raining (bool): whether it is raining or not
   
    Returns:
    str: "Wear a jacket" or "Do not wear a jacket"
    """
    if temp > 60 and raining == False:
        return "Do not wear a jacket"
    else:
        return "Wear a jacket"
print(jacket_checker(70, False))
# 6. Write a function that asks the user for a temperature and whether it is raining and then calls the jacket_checker function to tell the user whether they should wear a jacket or not. Your returned value should be the output of jacket_checker. Include Type Hinting and a Docstring.
def user_jacket_checker() -> str:
    temp = int(input("What is the temperature outside? "))
    raining = input("Is it raining outside? (Yes or no) ")
    if raining.lower() == "yes":
        raining = True
    else:
        raining = False
    output = jacket_checker(temp, raining)
    return output

print(user_jacket_checker())
# 7. Import the random module and write a function called random_number() that returns a random number between 1 and 10. Include Type Hinting and a Docstring.
import random 

def random_number():
    """returns a random number between 1 and 10
    
    Returns:
    int: random number between 1 and 10"""
    return random.randint(1, 10)
print(random_number())
# 8. Import floor from the math module (using from <module> import <function>) and write a function called round_down(num) that takes a number as a parameter (float) and returns the number rounded down to the nearest whole number. Include Type Hinting and a Docstring.
from math import floor
def round_down(num: float ) -> int:
    """takes in a float and returns the number rounded down to the nearest whole number
    
    args:
        num (float): the number to round down
    returns:
        int: whole number rounded down"""
    return floor(num)
print(round_down(5.5))