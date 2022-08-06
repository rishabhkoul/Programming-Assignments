import logging
logging.basicConfig(filename="Programming_Assignment6.log",level=logging.DEBUG,format ="%(asctime)s %(levelname)s %(message)s")

class assignment:
    # 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
    def fib(self,l):
        """Returns a list of fibonacci sequence of length l"""
        try:
            a=[]
            def fib_rec(n):
                if n<=1:
                    return n
                else:
                    return fib_rec(n-1) + fib_rec(n-2)
            for i in range(l):
                a.append(fib_rec(i))
            logging.info(a)
        except Exception as e:
            logging.info(e)
            logging.info('Please Enter a valid integer value')


    # 2. Write a Python Program to Find Factorial of Number Using Recursion?
    def factorial(self,n):
        """Returns the factorial of a number n"""
        try:
            def fact(n):
                if (n == 0) or (n == 1):
                    return 1
                return n*fact(n-1)
            logging.info(fact(n))
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a valid positive integer number")
    # 3. Write a Python Program to calculate your Body Mass Index?
    def bmi(self,height,weight):
        """Returns BMI of a person
            Takes two arguments height in meters and weight in kilograms"""
        error = "Please enter valid values of height in meters and weight in kilograms"
        try:
            bmi_value = weight / (height ** 2)
            if bmi_value > 25:
                logging.info(f"BMI of the person is {bmi_value:.2f}. The Person is Overweight.")
            elif bmi_value < 18.5:
                logging.info(f"BMI of the person is {bmi_value:.2f}. The Person is Underweight.")
            else:
                logging.info(f"BMI of the person is {bmi_value:.2f}. The Person is in healthy range.")
            return bmi_value

        except Exception as e:
            logging.error(e)
            logging.info(error)
    # 4. Write a Python Program to calculate the natural logarithm of any number?
    def nlog(self,n):
        """Returns the natural log of number n"""
        import math
        try:
            a = math.log(n)
            logging.info(f"Natural log of {n} is: {a:.4f}")
            return a
        except Exception as e:
            logging.error(e)


    # 5. Write a Python Program for cube sum of first n natural numbers?
    def cube_sum(self,n):
        """Return the sum of cubes of 1 to n natural numbers"""
        try:
            if n >= 1:
                sum = 0
                for i in range(1,n+1):
                    sum = sum + i**3
                logging.info(sum)
                return sum
            elif n <=0 :
                raise Exception("Error: Zero or Negative number entered")
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a valid positive natural number")



assign = assignment()

assign.fib(l=20)
assign.factorial(n=5)
assign.bmi(height=1.83,weight=120)
assign.nlog(n=10)
assign.cube_sum(n=10)