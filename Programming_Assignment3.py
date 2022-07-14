while True:
    try:
        #1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
        while True:
            try:
                a = int(input("\nEnter a number to know whether it is positive, negative or zero: "))
                if a > 0:
                    print("The number is : Positive")
                elif a < 0:
                    print("The number is : Negative")
                elif a == 0:
                    print("The number is : Zero")
                break
            except:
                print("Invalid entry. Please enter an integer value!")

        #2. Write a Python Program to Check if a Number is Odd or Even?
        while True:
            try:
                a = int(input("\nEnter a number to check whether it is Even or Odd: "))
                if a%2 == 0:
                    print(f"The number {a} is: Even")
                elif a%2 != 0:
                    print(f"The number {a} is: Odd")
                elif a == 0:
                    print("Number is: Zero")
                break
            except:
                print("Invalid Entry. Please enter a valid integer value ")

        #3. Write a Python Program to Check Leap Year?
        while True:
            try:
                a = int(input("\nEnter year to know if it is Leap year or not: "))
                if a%4 != 0:
                    print(f"{a} is not a Leap year")
                elif a%100==0:
                    if a%400==0:
                        print(f"{a} is a Leap year")
                    else:
                        print(f"{a} is not a Leap year")
                else:
                    print(f"{a} is a Leap year")
                break
            except:
                print("Invalid entry. Enter valid Year")

        #4. Write a Python Program to Check Prime Number?
        while True:
            try:
                a = int(input("\nEnter a number to check whether it is Prime or not: "))
                prime = 0
                if a !=0:
                    for i in range(2, a):
                        if a % i == 0:
                            prime = 1
                    if prime == 0:
                        print(f"The number {a} is Prime ")
                    else:
                        print(f"the number {a} is Not Prime ")
                    break
                else:
                    print("Enter a non Zero Integer Value")
            except:
                print("Invalid Entry. Enter a non Zero Integer Value")
        #5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
        while True:
            try:
                a = input("\nPress 'y' to print prime numbers between 1-10000 or 'n' to continue without printing: ").lower()
                if a == 'y':
                    for i in range(1,10000):
                        prime = 0
                        for j in range(2,i):
                            if i%j == 0:
                                prime = 1
                        if prime==0:
                            print(i,end=' ')
                    break
                elif a == 'n':
                    break
                else:
                    print("Please Enter 'y' or 'n' ")
            except:
                print("Invalid Entry. Please enter 'y' to print prime number or 'n' to continue without printing.")


        y_n = input("\nDo you want to rerun the program? Press 'y' to rerun or 'n' to exit: ").lower()
        if y_n == 'n':
            break
        elif y_n == 'y':
            pass
    except:
        print("\nInvalid entry! Enter 'y' or 'n'")

