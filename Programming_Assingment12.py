import logging
logging.basicConfig(filename="Programming_Assignment12.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
from collections import OrderedDict
dict1 = {'a':25,'b':350,'c':25,'d':[1,2,3,4],'e':'slow','f':25}
dict2 = {'a':25,'b':350,'c':85,'d':65}
dict3 = {'1':252,'2':353,'3':825,'4':265}
list1 = [('a',23),('b',12),('c',54)]
list2 = ['a','b','c','d']
list3 = [2,5,8,3]
dict4 = {'d':25,'b':350,'e':25,'c':525}
ordered_dict_ = OrderedDict([(1,'Value 1'),(2,'Value 2'),(3,'Value 3')])
item_to_insert = {4:'value 4'}
class DictOperations:

    # 1. Write a Python program to Extract Unique values dictionary values?

    def unique_dict(dict_):
        try:
            x = list(dict_.values())
            y =[]
            res = []
            for i in x:
                if type(i) == 'list':
                    y.extend(i)
                else:
                    y.append(i)
            
            for i in y:
                if i not in res:
                    res.append(i)

            logging.info(f"Unique values from the dictionary {dict_} are: {res}")
            return res
        except Exception as e:
            logging.error(e)

    # 2. Write a Python program to find the sum of all items in a dictionary?

    def sum_dict(dict_):
        try:
            x = list(dict_.values())
            s = []
            print(x)

            for i in x:
                if type(i) in [int,float] :
                    s.append(i)

            logging.info(f"Sum of items of dictionary {dict_} is = {sum(s)}")
            return s
        except Exception as e:
            logging.error(e)
    # 3. Write a Python program to Merging two Dictionaries?

    def merge_dict(dict_1,dict_2):
        try:
            for i in list(dict_2.keys()):
                dict_1[i] = dict_2[i]

            logging.info(f"After merging {dict_1} and {dict_2} we get \n {dict_1}")
            return dict_1
            
        except Exception as e:
            logging.error(e)
    # 4. Write a Python program to convert key-values list to flat dictionary?
    def to_dict(list_):
        try:
            x = dict(list_)
            logging.info(f"After converting list: {list_} to dictionary we get: {x}")
            return x
        except Exception as e:
            logging.error(e)
    # Alternate if we have two lists one keys and one values:
    def to_dict_from_lists(list_1,list_2):
        try:
            x = dict(zip(list_1,list_2))
            logging.info(f"merging key list: {list_1} with values list: {list_2} we get: {x}")
            return x
        except Exception as e:
            logging.error(e)



    # 5. Write a Python program to insertion at the beginning in OrderedDict?
    def insert_first(ordered_dict_,item_to_insert):
        """ordered_dict taked an ordered dictionary with key value pairs
        item_to_insert is a key value pair which to be inserted and moved to the beginning of the ordered list
         """
        try:
            ordered_dict = ordered_dict_
            item =item_to_insert
            ordered_dict.update(item_to_insert)
            ordered_dict.move_to_end(list(item_to_insert.keys()[0]))
            print(ordered_dict)
            logging.info(ordered_dict)
            return ordered_dict
        except Exception as e:
            logging.error(e)
            logging.info("Please enter valid ordered dictionary and valid key value pair")


    # 6. Write a Python program to check order of character in string using OrderedDict()?

    # 7. Write a Python program to sort Python Dictionaries by Key or Value?
    def sort_dict(dict_,by):
        """ by takes two values: 'key', 'value' by which the dict would by sorted
        """
        try:
            logging.info(f"Original dictionary: {dict_}")
            if by == 'key':
                x = dict(sorted(dict_.items(), key=lambda item: item[0]))
                logging.info(f"sorting by keys we get: {x}")
            elif by == 'value':
                x = dict(sorted(dict_.items(), key=lambda item: item[1]))
                logging.info(f"sorting by values we get: {x}")
                
            else:
                logging.error('Invalid entry for by')

            return x
        except Exception as e:
            logging.error(e)


DictOperations.unique_dict(dict1)
DictOperations.sum_dict(dict2)
DictOperations.merge_dict(dict2, dict3)
DictOperations.to_dict(list1)
DictOperations.to_dict_from_lists(list2, list3)
DictOperations.sort_dict(dict4, by='key')
DictOperations.sort_dict(dict4, by='value')
DictOperations.insert_first(ordered_dict_, item_to_insert)


