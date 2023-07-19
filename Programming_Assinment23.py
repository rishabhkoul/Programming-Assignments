import logging
logging.basicConfig(filename="Programming_Assignment23.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
import numpy as np

""" 
Question 1
Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True
""" 
def is_symmetrical(n):
    try:
        num = str(n)
        if num == num[::-1]:
            logging.info(f"The number {n} is symmmetrical: {True}")
            return True
        else:
            logging.info(f"The number {n} is symmetrical: {False}")
            return False
    except Exception as e:
        loggin.error(e)
"""
Question 2
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20
"""
def multiply_nums(string):
    try:
        numbers = list(map(int,string.split(", ")))
        output = np.product(numbers)
        logging.info(f"The product of digits if {string} = {output}")
        return output
    except Exception as e:
        loggin.error(e)
"""
Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
""" 
def square_digits(n):
    try:
        lst = [int(i)**2 for i in str(n)]
        output = int("".join(map(str,lst)))
        logging.info(f"square of digits of number {n} = {output}")
        return output
    except Exception as e:
        loggin.error(e)
"""
Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
""" 
def setify(lst):
    try:
        temp = []
        for i in lst:
            if i not in temp:
                temp.append(i)
        logging.info(f"After removing duplitcates from {lst} we get: {sorted(temp)}")
        return sorted(temp)
    except Exception as e:
        loggin.error(e)
"""
Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer.
"""
def mean(n):
    try:
        lst_n = [int(i) for i in str(n)]
        output = np.mean(lst_n)
        logging.info(f"Mean of digits of number {n} = {output}")
    except Exception as e:
        loggin.error(e)




if __name__ == "__main__":
    is_symmetrical(7227)
    is_symmetrical(12567)
    is_symmetrical(44444444)
    is_symmetrical(9939)
    is_symmetrical(1112111)

    multiply_nums("2, 3")
    multiply_nums("1, 2, 3, 4")
    multiply_nums("54, 75, 453, 0")
    multiply_nums("10, -2")

    square_digits(9119)
    square_digits(2483)
    square_digits(3212)

    setify([1, 3, 3, 5, 5])
    setify([4, 4, 4, 4])
    setify([5, 7, 8, 9, 10, 15])
    setify([3, 3, 3, 2, 1])

    mean(42)
    mean(12345)
    mean(666)