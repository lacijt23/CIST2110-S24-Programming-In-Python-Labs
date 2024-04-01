# Lab7
# Author: Laci Trull

## add in functions from test.py's test statements here to make the pytest work
## Use this file and your test plan to complete the lab

def calculate_rectangle_area(length: int, width: int):
    """ calculate the area of a rectangle
    Args:
        length (int): the length of the rectangle
        width (int): the width of the rectangle
        """
    length * width
    return length * width


def calculate_hypotenuse(a: int, b: int):
    """ calculate the hypotenuse of a right triangle
    Args:
        a (int): the length of one side of the triangle
        b (int): the length of the other side of the triangle
        """
    return (a**2 + b**2)**0.5

def is_even(number: int):
    """ check if a number is even
    Args:
        number (int): the number to check
        """
    return number % 2 == 0

def find_maximum(a: int, b: int):
    """ find the maximum of two numbers
    Args:
        a (int): the first number
        b (int): the second number
        """
    if a > b:
        return a
    else:
        return b
    
def grade_calculator(score: int):
    """ calculate the letter grade for a score using:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    
    Args:
        score (int): the score to grade
        """
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    print(calculate_rectangle_area(3, 4))
    print(calculate_hypotenuse(5, 12))
    print(is_even(2))
    print(find_maximum(3, 4))
    print(grade_calculator(90))


if __name__ == "__main__":
    main()
