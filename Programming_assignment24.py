import logging
logging.basicConfig(filename="Programming_Assignment24.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

from math import pi
""" 
Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
If the number cannot be divided evenly by 4, simply return the number.
Examples
amplify(4) ➞ [1, 2, 3, 40]
amplify(3) ➞ [1, 2, 3]
amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
Notes
The given integer will always be equal to or greater than 1.
Include the number (see example above).
To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.
""" 
def amplify(n):
    try:
        output = []
        output = [i*10 if i%4 == 0 else i for i in range(1,n+1)]
        """for i in range(1,n+1):
            if i % 4 == 0:
                output.append(i*10)
            elif i % 4 != 0:
                output.append(i)"""
        logging.info(f"Given number {n}, output list with numbers evenly divided y 4 amplified: {output}")
        return output
    except Exception as e:
        logging.error(e)



"""
Question2
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same.
""" 
def unique(lst):
    try:
        for i in lst:
            if lst.count(i) == 1:
                logging.info(f"unique number in the list {lst} is : {i}")
                return i
    except Exception as e:
        logging.error(e)

"""
Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
Examples
circy = Circle(11)
circy.getArea()
# Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
# Should return 27.897342763877365
Notes
Round results up to the nearest integer.
""" 
class Circle():

    def __init__(self,radius):
        self.radius = radius     
    
    def getArea(self):
        try:
            area = pi * self.radius ** 2
            logging.info(f"Area of a circle with radius {self.radius} is = {area}")
            return area
        except Exception as e:
            logging.error(e)
    
    def getPerimeter(self):
        try:
            perimeter = 2 * pi * self.radius
            logging.info(f"Area of a circle with radius {self.radius} is = {perimeter}")
            return perimeter
        except Exception as e:
            logging.error(e)

"""
Question4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.
Examples
sort_by_length(["Google", "Apple", "Microsoft"])
➞ ["Apple", "Google", "Microsoft"]
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
sort_by_length(["Turing", "Einstein", "Jung"])
➞ ["Jung", "Turing", "Einstein"]
Notes
All test cases contain lists with strings of different lengths, so you won't have to deal with multiple strings of the same length.
""" 
def sort_by_length(lst):
    try:
        output = sorted(lst,key=len)
        logging.info(f"original list {lst}, after sorting by length: {output}")
        return output
    except Exception as e:
        logging.error(e)
"""
Question5
Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.
Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25
is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169
is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
Notes
Numbers may not be given in a sorted order.
"""
def is_triplet(a,b,c):
    try:
        lst = tuple(sorted([a,b,c]))
        x,y,z = lst
        if x**2 + y**2 == z**2:
            logging.info(f"Given numbers {a,b,c} are Triplets: {True}")
            return True
        else:
            logging.info(f"Given numbers {a,b,c} are Triplets: {False}")
            return False
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    amplify(4)
    amplify(3)
    amplify(25)

    unique([3, 3, 3, 7, 3, 3])
    unique([0, 0, 0.77, 0, 0])
    unique([0, 1, 1, 1, 1, 1, 1, 1])


    circy = Circle(11)
    circy.getArea()
    # Should return 380.132711084365
    circy = Circle(4.44)
    circy.getPerimeter()
    # Should return 27.897342763877365

    sort_by_length(["Google", "Apple", "Microsoft"])
    sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
    sort_by_length(["Turing", "Einstein", "Jung"])

    is_triplet(3, 4, 5)
    is_triplet(13, 5, 12)
    is_triplet(1, 2, 3)
