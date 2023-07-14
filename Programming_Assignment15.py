import logging
logging.basicConfig(filename="Programming_Assignment15.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
"""
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
"""

def iter(n):
    try:
        for i in range(0,n):
            if (i%5 == 0 and i%7 == 0):
                yield i
    except Exception as e:
        logging.error(e)

def divb75(num):        
    lst = [str(i) for i in iter(num)]
    logging.info(",".join(lst))
    



"""
Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
"""
def iter_even(n):
    try:
        for i in range(n):
            if i%2 == 0:
                yield i
    except Exception as e:
        logging.error(e)

def even_numbers(n):
    try:
        lst = [str(i) for i in iter_even(n)]
        logging.info(",".join(lst))
    except Exception as e:
        logging.error(e)
            
"""
Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""

def fib_series(l):
    try:
        seq = [0,1]
        [seq.append(seq[k-1]+seq[k-2]) for k in range(2,l+1)]
        
        logging.info(','.join(list(map(str,seq))))
    except Exception as e:
        logging.error(e)
"""
Question 4:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
"""
def get_username(email):
    try:
        email_list = email.split('@')
        username = email_list[0]
        logging.info(username)
        return username
    except Exception as e:
        logging.error(e)

"""
Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    def __init__(self):
        pass
    def area(self):
        logging.info('0')
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def calculate_area(self):
        try:
            area = self.length ** 2
            logging.info(f"Area of shape is: {area}")
            return area
        except Exception as e:
            logging.error(e)
        






if __name__ == '__main__':
    num1 = int(input('Enter n value to find the numbers divisible by 5 and 7 upto n values: '))
    divb75(num1)

    num2 = int(input('Enter n value to find even numbers upto n value: '))
    even_numbers(num2)

    num3 = int(input("Enter n value to find the fibonacci sequence upto n values: "))
    fib_series(l=num3)
    
    email_address = input("Enter email address in username@domain.com format")
    get_username(email = email_address)
    len = int(input("Enter length of square to calculate the area: "))
    obj = Square(len)
    obj.calculate_area()