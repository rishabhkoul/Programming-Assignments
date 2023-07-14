import logging
logging.basicConfig(filename="Programming_Assignment17.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""
Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
""" 
def sum_div(a,b,c):
    try:
        temp = []
        for i in range(a,b+1):
            if i%c == 0:
                temp.append(i)
        if len(temp) < 1:
            logging.info(f"No numbers between {a},{b} are divisible by {c}")
        else:
            output = sum(temp)
            logging.info(f"Sum of numbers in range {a},{b} which are divisible by {c} = {output}")
            return output
    except Exception as e:
        logging.error(e)

"""
Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
""" 
def correct_signs(string):
    try:
        output = eval(string)
        logging.info(f"The expression in '{string}' is {output}")
        return output
    except Exception as e:
        logging.error(e)

"""
Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
""" 
import re
def replace_vowels(string,replaced):
    try:
        output = re.sub("[aeiouAEIOU]",replaced,string)
        logging.info(f"After replacing vowels in {string} with {replaced} we get: {output}")
        return output
    except Exception as e:
        logging.error(e)


"""
Question4. Write a function that calculates the factorial of a number recursively.
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
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
"""
def hamming_distance(text1,text2):
    try:
        counter = 0
        i = 0
        while i < len(text1):
            if (text1[i] != text2[i]):
                counter += 1
            i += 1
        logging.info(f"hamming distance between {text1} and {text2} is : {counter}")
        return counter
    except Exception as e:
        logging.error(e)




if __name__ == "__main__":
    sum_div(1, 10, 20)
    sum_div(1, 10, 2)
    sum_div(1, 10, 3)

    correct_signs("3 < 7 < 11")
    correct_signs("13 > 44 > 33 > 1")
    correct_signs("1 < 2 < 6 < 9 > 3")

    replace_vowels("the aardvark", "#")
    replace_vowels("minnie mouse", "?")
    replace_vowels("shakespeare", "*")

    factorial(5)
    factorial(3)
    factorial(1)
    factorial(0)

    hamming_distance("abcde", "bcdef")
    hamming_distance("abcde", "abcde")
    hamming_distance("strong", "strung")
