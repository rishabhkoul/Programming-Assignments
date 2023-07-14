import logging
logging.basicConfig(filename="Programming_Assignment13.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

"""Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

def calculate_value(t):
    try:
        c = 50
        h = 30
        output = []
        for i in list(t.split(',')):
            d = int(i)
            q = ((2*c*d)/h)**0.5
            output.append(int(q))
        print(','.join(map(str,output)))
        logging.info(','.join(map(str,output)))
        return output
    except Exception as e:
        logging.error(e)




"""
Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
def make_array(i,j):
    try:
        rows,cols = (i,j)

        arr = [[a*b for a in range(cols)] for b in range(rows)]
        logging.info(arr)
        print(arr)
        return arr
    except Exception as e:
        logging.error(e)



"""
Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world """

def sorted_words(words):
    try:
        words_list = list(x.split(','))
        sorted_list = sorted(words_list)
        print(",".join(sorted_list))
        logging.info(",".join(sorted_list))
        return sorted_list
    except Exception as e:
        logging.error(e)






"""
Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

def processed_words(words):
    try:
        s = words.lower().split()
        k = []
        for i in s:
            if (words.count(i) >= 1) and (i not in k):
                k.append(i)
        sorted_words = sorted(k)
        output= " ".join(sorted_words)
        print(output)
        logging.info(output)
        return output
    except Exception as e:
        logging.error(e)




"""
Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10

DIGITS 3"""
def count_letter_digit(sentence):
    try:
        char = sentence.lower()
        letters = [] 
        digits = []
        for i in char:
            if str(i).isalpha():
                letters.append(i)
            elif str(i).isnumeric():
                digits.append(i)
        
        print(f"Letters = {len(letters)}\nDigits = {len(digits)}")
        logging.info(f"Letters = {len(letters)}\nDigits = {len(digits)}")
        report = (len(letters),len(digits))
        return report
    except Exception as e:
        logging.error(e)



"""
Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

"""
def check_password(enter_passwords):
    try:
        passwords = enter_passwords.split(',')
        
        print(passwords)
        logging.info(f"Passwords are {passwords}")
        valid_passwords = []

        for string in passwords:
            u,l,n,s = 0,0,0,0
            if (len(string) in range(6,13)):
                for j in string:
                    if (j.isupper()):
                        u += 1
                    if (j.islower()):
                        l += 1
                    if (j.isdigit()):
                        n += 1
                    if (j=='$' or j=='#' or j=="@"):
                        s += 1
            if (u >=1 and l >=1 and n >= 1 and s >= 1 and u+l+n+s == len(string)):
                print(f"{string} is a Valid Password")
                valid_passwords.append(string)
            else:
                print(f"{string} is an Invalid Password")
        logging.info(','.join(valid_passwords))
        return ','.join(valid_passwords)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':

    t = input("Enter comma separated numbers to calculate output: ")
    calculate_value(t)


    make_array(3,5)

    x = input("Enter comma separated words to arrange them alphabetically: ")
    sorted_words(x)

    y = input("Enter whitespace separated words to remove duplicates and arange alphaumericaly: ")
    processed_words(y)

    z = input("Enter a sentence to know the number of digits and letters: ")
    count_letter_digit(sentence=z)

    passwords_ = input("Enter comma separated passwords to check if they are valid or not: ")
    check_password(enter_passwords=passwords_)