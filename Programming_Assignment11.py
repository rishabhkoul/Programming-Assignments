import logging
logging.basicConfig(filename="Programming_Assignment11.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

class StringOperations:
    # 1. Write a Python program to find words which are greater than given length k?
    def find_words(self,string,k = 0):

        """Returns words which are greater than length k
            Takes two arguments a sequence of words and length k
            Default value of k is 0, If not specified the function will return words with length greater than 0"""
        try:
            output = ' '.join([i for i in string.split() if len(i) > int(k)])
            logging.info(f"Words which have length greater than {k} are: {output}")
            return output
        except Exception as e:
            logging.error(e)
            logging.error("Please enter valid string value and valid integer length value")


    # 2. Write a Python program for removing i-th character from a string?
    def remove_character(self,string,i):
        """Returns the string with the ith character removed"""
        try:
            with_removed = string[0:int(i)] + string[int(i) + 1:]
            logging.info(f"After removing {i}th character from the string we get: {with_removed}")
            return with_removed
        except Exception as e:
            logging.error(e)
            logging.error("Please enter valid string value and valid integer value in i")


    # 3. Write a Python program to split and join a string?
    def split_join(self,string):
        """Returns a split string"""
        try:
            split = string.split()
            join_str = ' '.join(split)
            logging.info(f"After splitting the string we get: {split}")
            logging.info(f'After Joining the split string we get: {join_str} ')
            return split
        except Exception as e:
            logging.error(e)
            logging.error("Please Enter a valid string")


    # 4. Write a Python to check if a given string is binary string or not?
    def binary_string(self,string):
        """This function shows if a string is binary string or not """
        try:
            flag = 'Not Binary'

            for i in string:
                if i not in ('01'):
                    flag = "Not Binary"
                    break
                else:
                    flag = "Binary"
            logging.info(f"String: {string} is {flag}")
            return flag
        except Exception as e:
            logging.error(e)
            logging.error("Please enter a valid string")




    # 5. Write a Python program to find uncommon words from two Strings?
    def uncommon_words(self,a,b):
        """Returns uncommon words from two strings a and b"""
        try:
            uncommon = ''
            for i in a.lower().split():
                if i not in b.lower().split():
                    uncommon = uncommon + ' ' + i
            for j in b.lower().split():
                if j not in a.lower().split():
                    uncommon = uncommon + ' ' + j
            logging.info(f"The uncommon words from the strings: '{a}' and '{b}' are : {uncommon}")
            return uncommon
        except Exception as e:
            logging.error(e)
            logging.error("Please enter valid string arguments in the function")

    # 6. Write a Python to find all duplicate characters in string?
    def duplicate_char(self,string):
        """Returns the duplicate characters in a string"""
        try:
            dup = ""
            for i in string:
                if string.lower().count(i) == 1:
                    dup = dup + '' + i
            logging.info(f"After Removing Duplicate characters from: '{string}' we get: {dup}")
            return dup
        except Exception as e:
            logging.error(e)
            logging.error("Please enter valid string arguments in the function")
    # 7. Write a Python Program to check if a string contains any special character?
    def special_char(self,string):
        """This function tells if there are any special characters in a string or not"""
        from string import punctuation
        punct = set(punctuation)
        try:
            special_chars = ''
            special = 'This string does not Contain Special Characters'
            for i in string:
                if i in punct:
                    special_chars = special_chars + " " + i
                    special = "This string contains Special Characters"
            logging.info(special)
            logging.info(f"The special characters in the string: '{string}' are: {special_chars}")
            return special

        except Exception as e:
            logging.error(e)
            logging.error("Please enter valid string arguments in the function")


ops = StringOperations()
ops.find_words(string="# 1. Write a Python program to find words which are greater than given length k?",k=4)
ops.remove_character("0123456789",i=5)
ops.split_join("Python program to find words which are")
ops.binary_string('010110111')
ops.binary_string('010185611')
ops.uncommon_words(a="Checking for uncommon words in two string",b="Common Words will be removed from two strings")
ops.duplicate_char("abcdabcjkkrts ABCDl")
ops.special_char("$tring % & #ouse ()")
ops.special_char("Nothing found here")