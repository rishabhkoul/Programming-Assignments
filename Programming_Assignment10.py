import logging
logging.basicConfig(filename="Programming_Assignment_10.log",level=logging.DEBUG,format= "%(asctime)s %(levelname)s %(message)s")
a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,[35,52,23],[12,3],[],23,[],543,2,2,[]]
c = ['as','2',2,3,4]
class list_operations:
    #1. Write a Python program to find sum of elements in list?
    def sum_list(self,lst):
        try:
            sum = 0
            for i in lst:
                sum = sum+i
            logging.info(f'Sum of List is {sum}')
            return sum
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")

    # Alternate Direct Method
    # logging.info(sum(a))

    #2. Write a Python program to Multiply all numbers in the list?
    def product(self,lst):
        try:
            product = 1
            for i in lst:
                product = product * i
            logging.info(f"After multiplying all numbers in the list we get: {product}")
            return product
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")

    #3. Write a Python program to find smallest number in a list?
    def smallest(self,lst):
        try:
            small = sorted(lst)[0]
            logging.info(f"Smallest number in the list is {small}")
            return small
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")


    # alternate Method
    # logging.info(min(a))


    #4. Write a Python program to find largest number in a list?
    def largest(self,lst):
        try:
            large = sorted(lst)[-1]
            logging.info(f"Largest number in the list is {large}")
            return large
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")

    # alternate method
    # logging.info(max(a))

    #5. Write a Python program to find second largest number in a list?
    def second_largest(self,lst):
        try:
            second_large = sorted(lst)[-2]
            logging.info(f"Second Largest number in the list is {second_large}")
            return second_large
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")


    #6. Write a Python program to find N largest elements from a list?
    def largest_num(self,lst,n):
        try:
            sorted_list=[]
            for i in range(1,n+1):
                sorted_list.append(sorted(lst)[-i])
            logging.info(f'N largest numbers from the List are: {sorted_list}')
            return sorted_list
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")
    #7. Write a Python program to print even numbers in a list?
    def even(self,lst):
        try:
            even_list = [i for i in lst if i%2 == 0]
            logging.info(f"Even numbers from the list are: {even_list}")
            return even_list
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")

    #8. Write a Python program to print odd numbers in a List?
    def odd(self,lst):
        try:
            odd_list = [i for i in lst if i%2 != 0]
            logging.info(f"Odd numbers from the list are: {odd_list}")
            return odd_list
        except Exception as e:
            logging.error(e)
            logging.info("Please enter a list with only numbers")


    #9. Write a Python program to Remove empty List from List?
    def remove_empty_list(self,lst):
        try:
            for i in lst:
                if (type(i) == list) and (len(i) == 0):
                    lst.remove(i)
            logging.info(lst)
        except Exception as e:
            logging.error(e)


    #10. Write a Python program to Cloning or Copying a list?
    def copy_list(self,lst):
        try:
            copy = [i for i in lst]
            logging.info(f"Copy of list is: {copy}")
            return copy
        except Exception as e:
            logging.error(e)
    # Alternate method
    # copy = list_name.copy()
    # copy = list_name[:]


    #11. Write a Python program to Count occurrences of an element in a list?

    def count_in_list(self,lst,item):
        try:
            c = 0
            for i in lst:
                if i == item:
                    c += 1
            logging.info(c)
            return c
        except Exception as e:
            logging.error(e)

    # Alternate method
    #list_name.count(10)

ops = list_operations()

ops.sum_list(lst=a)
ops.product(lst=a)
ops.smallest(lst=a)
ops.largest(lst=a)
ops.second_largest(lst=a)
ops.largest_num(lst=a,n=4)
ops.even(lst=a)
ops.odd(lst=a)
ops.remove_empty_list(lst=a)
ops.copy_list(lst=a)
ops.count_in_list(lst=a,item=2)


ops.sum_list(lst=c)
ops.product(lst=c)
ops.smallest(lst=c)
ops.largest(lst=c)
ops.second_largest(lst=c)
ops.largest_num(lst=c,n=4)
ops.even(lst=c)
ops.odd(lst=c)
ops.remove_empty_list(lst=c)
ops.copy_list(lst=c)
ops.count_in_list(lst=c,item=2)
