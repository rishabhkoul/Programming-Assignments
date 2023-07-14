import logging
logging.basicConfig(filename="Programming_Assignment16.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")


"""
1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
"""
n = 1997
years_list = [i for i in range(n,n+6)]
logging.info(f"List having year of birth and each year upto fifth birthday: {years_list}")
"""
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
"""
third_birthday = years_list[3]
logging.info(f"Third birthday is the year : {third_birthday}")

"""
3. In the years list, which year were you the oldest?
""" 
oldest = max(years_list)
logging.info(f"year in which the oldest is : {oldest}")

"""
4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
""" 
things = ["mozzarella","cinderella","salmonella"]
logging.info(f"Things list is: {things}")
"""
5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
"""
things[1].capitalize()
logging.info(f"after capitalizing the 2nd element in the list: {things}\n Note: the element does not change")
print(things)
"""
6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
""" 
surprise = ["Groucho","Chico,","Harpo"]
logging.info(f"surprise list is: {surprise}")
"""
7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
""" 
reversed_capitalized = surprise[-1][::-1].capitalize()
logging.info(f"First reverse then capitalized: {reversed_capitalized}")
"""
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
""" 
e2f = {'dog':"chien","cat":"chat","walrus":"morse"}
logging.info(f"English to french dictionary with 3 words: {e2f}")
"""
9. Write the French word for walrus in your three-word dictionary e2f.
""" 
logging.info(f"french word for 'walrus' is: {e2f['walrus']}")
"""
10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
""" 
f2e = {}
for i,j in e2f.items():
    f2e[j] = i
logging.info(f"French to english dictionary with 3 words: {f2e}")
"""
11. Print the English version of the French word chien using f2e.
""" 
logging.info(f"english word for 'chien' is : {f2e['chien']}")
"""
12. Make and print a set of English words from the keys in e2f.
""" 
a = []
for i in e2f.keys():
    a.append(i)
a = set(a)
logging.info(f"set of english words : {a}")
"""
13. Make a multilevel dictionary called life.
Use these strings for the topmost keys: 'animals', 'plants', and 'other'. 
Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. 
Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. 
Make all the other keys refer to empty dictionaries.
""" 
life= {"animals":{"cats":['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'others':{}}
logging.info(f"Life dictionary : {life}")
"""
14. Print the top-level keys of life.
""" 
logging.info(f"top level keys of dictionary life are: {life.keys()}")
"""
15. Print the keys for life['animals'].
""" 
logging.info(f"Keys of animals dictionary: {life['animals'].keys()}")

"""
16. Print the values for life['animals']['cats']
"""
logging.info(f"Values for life['animals']['cats] is : {life['animals']['cats']}")

if __name__ == '__main__':
    pass