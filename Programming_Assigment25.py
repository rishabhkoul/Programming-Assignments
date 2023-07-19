import logging
logging.basicConfig(filename="Programming_Assignment25.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
import re
""" 
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.
""" 
def equal(a,b,c):
    try:
        lst = [a,b,c]
        for i in lst:
            if lst.count(i) > 1:
                logging.info(f"Given integers are {a,b,c}. Number of equal values: {lst.count(i)}")
                break
                return lst.count(i)
            else:
                logging.info(f"Given integers are {a,b,c}. Number of equal values: {0}")
                return 0
    except Exception as e:
        logging.error(e)
"""
Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order.
""" 
def dict_to_list(dict_):
    try:
        #output = list(zip(dict_.keys(),dict_.values()))
        output = list(dict_.items())
        logging.info(f"Original dictionary: {dict_}. List of key value pairs: {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase.
""" 
def mapping(lst):
    try:
        output = {}
        for i in lst:
            output[i] = i.upper()
        logging.info(f"original list: {lst}. dictionry of string with key value as lowercase: uppercase : {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
""" 
def vow_replace(string,vowel):
    try:
        output = re.sub("[aeiouAEIOU]", vowel, string)
        logging.info(f"original string: {string}. After replacing vowels with {vowel} we get: {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
"""
def ascii_capitalize(string):
    try:
        temp = [i.upper() if ord(i) % 2 ==0 else i.lower() for i in string]
        output = "".join(temp)
        logging.info(f"original String: {string}. After capitalizing even ASCII code characters we get: {output}")
        return output
    except Exception as e:
        logging.error(e)



if __name__ == "__main__":
    equal(3, 4, 3)
    equal(1, 1, 1)
    equal(3, 4, 1) 

    dict_to_list({"D": 1,"B": 2,"C": 3})
    dict_to_list({"likes": 2,"dislikes": 3,"followers": 10})

    mapping(["p", "s"])
    mapping(["a", "b", "c"])
    mapping(["a", "v", "y", "z"])

    vow_replace("apples and bananas", "u")
    vow_replace("cheese casserole", "o")
    vow_replace("stuffed jalapeno poppers", "e")

    ascii_capitalize("to be or not to be!")
    ascii_capitalize("THE LITTLE MERMAID")
    ascii_capitalize("Oh what a beautiful morning.")