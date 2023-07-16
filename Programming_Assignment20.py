import logging
logging.basicConfig(filename="Programming_Assignment20.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""
Question1
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []
""" 
def filter_list(lst):
    try:
        output = [i for i in lst if type(i) != str]
        logging.info(f"Initial lisst: {lst}. After removing strings: {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question2
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
""" 
def add_indexes(lst):
    try:
        output = [lst.index(i) + i for i in lst]
        logging.info(f"Initial List: {lst}. After adding index to the elements e get: {output}")
        return output
    except Exception as e:
        logging.error(e)

"""
Question3
Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
""" 
def cone_volume(h,r):
    try:
        pi = 3.1415
        volume = (pi * r * r * h)/3
        logging.info(f"Volume of a cone with height = {h} and radius = {r} is = '{round(volume,2)}'")
        return round(volume,2)
    except Exception as e:
        logging.error(e)
"""
Question4
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are: 
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the sequence.
Examples
triangle(1) ➞ 1
triangle(6) ➞ 21
triangle(215) ➞ 23220
""" 

def triangle(n):
    try:
        x = 0
        for i in range(1,n+1):
            x = x+i
        logging.info(f"Number of dots in a triangular sequence of length {n} is: {x}")
        return x
    except Exception as e:
        logging.error(e)
"""
Question5
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
"""
def missing_num(lst):
    try:
        output = [i for i in range(1,11) if i not in lst]
        logging.info(f"Missing digit between 1 to 10 in the list: {lst} is: {output[0]}")
        return output[0]
    except Exception as e:
        logging.error(e)




if __name__ == "__main__":
    filter_list([1, 2, 3, "a", "b", 4])
    filter_list(["A", 0, "Edabit", 1729, "Python", "1729"])
    filter_list(["Nothing", "here"])

    add_indexes([0, 0, 0, 0, 0])
    add_indexes([1, 2, 3, 4, 5])
    add_indexes([5, 4, 3, 2, 1])

    cone_volume(3, 2)
    cone_volume(15, 6)
    cone_volume(18, 0)

    triangle(1)
    triangle(6)
    triangle(215)

    missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])
    missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])
    missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])