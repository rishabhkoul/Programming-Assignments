import logging
logging.basicConfig(filename="Programming_Assignment19.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""
Question1
Create a function that takes a string and returns a string in which each character is repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
double_char("1234!_ ") ➞ "11223344!!__  "
"""
def double_char(text):
    try:
        lst = [i*2 for i in text]
        output = "".join(lst) 
        logging.info(f"Initial Text: {text}. After doubling the characters:{output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question2
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"
""" 
def reverse(b):
    try:
        if b == True:
            logging.info("Initial bool value: {b}. After reversing {False}")
            return False
        elif b == False:
            logging.info("Initial bool value: {b}. After reversing {True}")
            return True
        else:
            logging.info("Please enter a boolean value")
            return "Enter a boolean value"
    except Exception as e:
        logging.error(e)
"""
Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)

num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
""" 
def num_layers(layers):
    try:
        thickness = 0.5
        output = 0
        for i in range(1,layers+1):
            thickness = thickness*2
            output = thickness
        logging.info(f"thickness of paper in meters folded {layers} times is : {output/1000}")
        return output
    except Exception as e:
        logging.error(e)

"""
Question4
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]
index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
index_of_caps("determine") ➞ []
index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
index_of_caps("sUn") ➞ [1]
""" 
def index_of_caps(text):
    try:
        lst = [text.index(i) for i in text if i.isupper()]
        logging.info(f"index of capital letters in {text}is : {lst}")
        return lst
    except Exception as e:
        logging.error(e)
"""
Question5
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]
"""
def find_even_nums(num):
    try:
        output = [i for i in range(1,num+1) if i%2 == 0]
        logging.info(f"even numbers from 1 to {num} are : {output}")
        return output
    except Exception as e:
        logging.error(e)




if __name__ == "__main__":
    double_char("String")
    double_char("Hello World!")
    double_char("1234!_ ")

    reverse(True)
    reverse(False)
    reverse(0)
    reverse(None)

    num_layers(1)
    num_layers(4)
    num_layers(21)

    index_of_caps("eDaBiT")
    index_of_caps("eQuINoX")
    index_of_caps("determine")
    index_of_caps("STRIKE")
    index_of_caps("sUn")

    find_even_nums(8)
    find_even_nums(4)
    find_even_nums(2)