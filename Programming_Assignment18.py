import logging
logging.basicConfig(filename="Programming_Assignment18.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""
Question 1
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
"""
def filter_list(lst):
    try:
        output = [i for i in lst if type(i) != str]
        logging.info(f"after filtering srings from list {lst} we get: {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question 2
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
""" 
def reverse(text):
    try:
        output = text[::-1]
        logging.info(f"Input text = {text}. After reversing output= {output}")
        return output
    except Exception as e:
        logging.error(e)

"""
Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]

print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
first  ➞ 1

middle ➞ [2, 3, 4, 5]

last ➞ 6
Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.
""" 
def list_parts(lst):
    try:
        first,*middle,last = lst
        logging.info(f"Given list is {lst}\nfirst= {first}, middle= {middle}, last= {last} ")
        return first,middle,last
    except Exception as e:
        logging.error(e)
"""
Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1
""" 
def factorial(n):
    try:
        if n == 1 or n == 0:
            logging.info(f'Factorial of {n} is {1}')
            return 1
        else:
            output = n * factorial(n-1)
            logging.info(f'factorial of {n} is {output}')
            return output
    except Exception as e:
        logging.error(e)

"""
Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
"""
def move_to_end(lst,item):
    try:
        logging.info(f"Initial list {lst}. Item to be moved {item}")
        lst = lst
        for i in lst:
            if i == item:
                lst.append(lst.pop(lst.index(item)))
        logging.info(f"After moving the final list = {lst}")
        return lst
    except Exception as e:
        logging.error(e)



if __name__ == "__main__":
    filter_list([1, 2, "a", "b"])
    filter_list([1, "a", "b", 0, 15])
    filter_list([1, 2, "aasf", "1", "123", 123])

    reverse("Hello World")
    reverse("ReVeRsE")
    reverse("Radar")

    factorial(5)
    factorial(3)
    factorial(1)
    factorial(0)

    move_to_end([1, 3, 2, 4, 4, 1], 1)
    move_to_end([7, 8, 9, 1, 2, 3, 4], 9)
    move_to_end(["a", "a", "a", "b"], "a")

    list_parts("writeyourcodehere")
