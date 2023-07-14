import logging
logging.basicConfig(filename="Programming_Assignment14.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""
Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
class iter:
    def __init__(self,n):
        self.n = n
    def divb7(self):
        try:
            for i in range(0,self.n):
                if i%7 == 0:
                    yield i
        except Exception as e:
            logging.error(e)

"""
Question 2:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
def frequency_words(sentence):
    try:
        words = sorted(sentence.split())
        freq = {}
        for i in sorted(set(words)):
            freq[i] = words.count(i)
        print(freq)
        logging.info(f"frequency of words are:\n{freq}")
        return freq 
    except Exception as e:
        logging.error(e)
"""
Question 3:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""
class person:
    def getgender(self):
        try:
            pass
        except Exception as e:
            logging.error(e)

class male(person):
    def getgender(self):
        try:
            print("Male")
            logging.info('Male')
        except Exception as e:
            logging.error(e)
class female(person):
    def getgender(self):
        try:
            logging.info("female")
            print("Female")
        except Exception as e:
            logging.error(e)

"""
Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""
def generate_sentence():
    try:
        subject = ['I','You']
        verb = ['Play','Love']
        objects = ['Hockey','Football']

        for i in subject:
            for j in verb:
                for k in objects:
                    logging.info(i,j,k)
                    print(i,j,k) 
    except Exception as e:
        logging.error(e)
"""
Question 5:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""
import zlib
def comp_decomp(string):
    try:
        text = string
        logging.info(f"text to be compressed: {text}")
        compressed_text = zlib.compress(text)
        logging.info(f"Compressed text: {compressed_text}")

        logging.info(f"text to decompress {compressed_text}")
        decompressed_text = zlib.decompress(compressed_text)
        logging.info(f"decompressed text: {decompressed_text}")

        print(compressed_text)

        return compressed_text
    except Exception as e:
        logging.error(e)
"""
Question 6:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"""
def binary_search(list_,n):
    try:
        list1 = sorted(list_)
        logging.info(f"Searching index of {n} in the list {list1}")
        low = 0
        mid = 0
        high = len(list1)-1
        while low <= high:
            mid = (low + high)//2

            if list1[mid] < n:
                low = mid + 1

            elif list1[mid] > n:
                high = mid - 1

            else:
                print(mid)
                logging.info(f'Location of element {n} is:{mid}')
                return mid
        logging.info('Element not in the list')                
        return -1


    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    #creating an oject of iter class, n is the value of range of generator
    iter_object = iter(n=100)
    iter_object.divb7() # this method will create a generator of 0 to n range of numbers divisible by 7
    div_by_7 = [i for i in iter_object.divb7()]
    logging.info(div_by_7)
    print(div_by_7)

    x = input("Enter a sentence to know the frequency of the words: ")
    frequency_words(sentence=x)    

    obj_male = male()
    obj_female = female()

    obj_male.getgender()
    obj_female.getgender()


    to_comp = b"hello world!hello world!hello world!hello world!"
    comp_decomp(string=to_comp)

    to_search_list = [20,40,67,82,23,98,12,56,32,66,5,3,10,69]
    search_number = 66

    binary_search(to_search_list,search_number)