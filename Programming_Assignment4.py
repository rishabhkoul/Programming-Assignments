while True:
    try:
        #1. Write a Python Program to Find the Factorial of a Number?
        while True:
            try:
                a = int(input("\nEnter a value to find factorial: "))
                if a <= 0:
                    print("Please enter a positive integer")
                else:
                    s=1
                    for i in range(a - 1, 1, -1):
                        s = s * i
                    print(f"The factorial of {a} is: ",s)
                    break
            except:
                print("Enter a valid integer value")
        #2. Write a Python Program to Display the multiplication Table?
        while True:
            try:
                a = int(input("\nEnter a number to show multiplication table upto 10: "))
                for i in range(1,11):
                    print(f"{a} x {i} = {a * i}")
                break
            except:
                print('Invalid entry. Enter a valid integer value.')
        #3. Write a Python Program to Print the Fibonacci sequence?
        while True:
            try:
                num = int(input("\nEnter a value upto which elements to show Fibonacci Sequence: "))
                a = 1
                b = 1
                if num <= 0:
                    print("Please enter a positive integer value")
                else:
                    for i in range(abs(num)):
                        print(a, end=" ")
                        a, b = b, a + b
                    break
            except:
                print("Invalid Entry. Please enter a valid integer value")
        #4. Write a Python Program to Check Armstrong Number?
        while True:
            try:
                num = input("\nEnter a value to check if it is an armstrong number: ")
                if int(num) == 0:
                    print("Please enter a non zero number")
                elif int(num)!= 0:
                    a = list(map(int, num))
                    power = [i ** len(a) for i in a]
                    if sum(power) == int(num):
                        print(f"The number {num} is an Armstrong number")
                    elif sum(power) != int(num):
                        print(f"The number {num} is not an Armstrong number")
                    break
            except:
                print("Invalid Entry. Please enter a valid number")

        #5. Write a Python Program to Find Armstrong Number in an Interval?
        while True:
            try:
                number_range = input("Enter the range between which you want Armstrong Numbers in space separated format.Example: 1 500 ")
                x,y = map(int,number_range.split())
                if x <= 0 or y<=0:
                    print("Please Enter positive integer values")
                else:
                    for i in range(x,y):
                        power = len(str(i))
                        temp = i
                        sum = 0
                        while temp > 0:
                            digit = temp % 10
                            sum += digit ** power
                            temp //= 10
                        if sum == i:
                            print(i)
                    break
            except:
                print("Invalid Entry. Enter a valid space separated range values.Example 50 5000")

        #6. Write a Python Program to Find the Sum of Natural Numbers?
        while True:
            try:
                a = int(input("\nEnter a natural number to find the sum upto the number: "))
                sum = 0
                if a <= 0:
                    print("Natural numbers cant be negative or zero. Please Enter Again")
                elif a > 0:
                    for i in range(a+1):
                        sum = sum+i
                    print(f'Sum of {a} natural numbers is: ',sum)
                    break
            except:
                print("Invalid Entry. Please enter a valid natural number ")
        y_n= input("\nDo you want to rerun the program? Press 'y' to rerun and 'n' to exit: ").lower()
        if y_n == 'n':
            break
        elif y_n == 'y':
            pass
    except:
        print("Invalid entry. Enter 'y' or 'n' only.")

