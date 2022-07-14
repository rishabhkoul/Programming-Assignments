while True:
    #1. Write a Python program to convert kilometers to miles?
    while True:
        try:
            a = float(input("\nEnter Kilometers to convert to miles: "))
            b = 0.621371*a
            print(f"{a} kms in miles is: {b} miles")
            break
        except:
            print("Please enter a Number ")
    #2. Write a Python program to convert Celsius to Fahrenheit?
    while True:
        try:
            a = float(input("\nEnter temperature in Celsius: "))
            b = (a*1.8)+32
            print(f"{a} Celsius is equal to {b} fahrenheit")
            break
        except:
            print("Please enter valid temperature")
    #3. Write a Python program to display calendar?
    import calendar

    while True:
        try:
            date = input("\nEnter the year and month to show calender in format YYYY MM. Example 2015 02 ")
            year, month_ = map(int, date.split())
            print(calendar.month(year, month_))
            break
        except:
            print("Enter valid year and month in YYYY MM format.Example 1965 12")
            print("Month value should be between 1 and 12")

    #4. Write a Python program to solve quadratic equation?
    while True:
        try:
            coeff = input("\nEnter coefficients a,b,c of quadratic equation ax^2+bx+c. Enter in space separated format. Example: 2 10 1 ")
            a,b,c = map(float,coeff.split())
            print(f"Your entered equation is ({a})x^2+({b})x+({c})")
            dis = (b**2)-4*a*c
            sol1= (-b+(dis**0.5))/(2*a)
            sol2= (-b-(dis**0.5))/(2*a)
            print(f"Solutions of x are ({sol1:.3f}) and ({sol2:.3f})")
            break
        except ZeroDivisionError:
            print("Value of 'a' cannot be Zero. Enter a non zero coefficient of x^2")
        except:
            print("Please enter 3 numeric values")


    #5. Write a Python program to swap two variables without temp variable?
    while True:
        try:
            num = input("\nEnter Two numbers to be swapped ")
            a,b = map(int,num.split())
            print(f"Entered numbers a,b are ",a,b)
            a,b = b,a
            print(f"After Swapping. The values of a and b are ",a,b)
            break
        except:
            print("Please enter two integer values with one space in between. Example 10 25")
    try:
        y_n = input("\nDo you want to rerun the program.Type 'y' to rerun and 'n' to exit ").lower()
        if y_n == 'n':
            break
        elif y_n == 'y':
            pass
    except:
        print("type only 'y' or 'n")