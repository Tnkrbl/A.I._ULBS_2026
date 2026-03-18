print(type(1))    # int
print(type(-10))  # int
print(type(0))    # int
print(type(0.0))  # float
print(type(2.2))  # float
print(type(4E2))  # float - 4*10 to the power of 2

# Arithmetic

print(10 + 3)     # 13
print(10 - 3)     # 7
print(10 * 3)     # 30
print(10 ** 3)    # 1000
print(10 / 3)     # 3.33333333333333335
print(10 // 3)    # 3 --> floor division - no decimals and returns an int
print(10 % 3)     # 1 --> modulo operator - return the reminder. Good for deciding if
                  #       number is even or odd

# Basic Functions

print(pow(5,2))         # 25 --> like doing 5**2
print(abs(-50))         # 50
print(round(5.46))      # 5
print(round(5.468, 2))  # 5.47 --> round to nth digit
print(bin(512))         # '0b1000000000' --> binary format
print(hex(512))         # '0x200' - hexadecimal format

# Converting Strings to Numbers

# age = input("How old are you? ")          --> commented so no input required on Run
# age = int(age)                            --> commented so no input required on Run
# pi = input("What is the value of pi? ")   --> commented so no input required on Run
# pi = float(pi)                            --> commented so no input required on Run

# Strings

print(type('Helloooooo'))          # str

print('I\'m thirsty')
print("I'm thirsty")
print("\n")                        # new line
print("\t")                        # adds a tab

print('Hey you!'[4])               # y
name = 'John Doe'
print(name[2])                     # h
print(name[:])                     # John Doe
print(name[1:])                    # ohn Doe
print(name[:1])                    # J
print(name[-1])                    # e
print(name[::1])                   # John Doe
print(name[::-1])                  # eoD njoJ
print(name[0:7:2])                 # Jh o
# : is called slicing and has the format [ start: end : step ]

print('Hi there ' + 'Timmy')  # 'Hi there Timmy' --> This is called string concatenation
print('*'*10)                 # *********

# Basic Functions

print(len('turtle'))                 # 6

# Basic Methods

print('  I am alone '.strip())      # 'I am alone' --> Strips all whitespace characters
                                    #                  from both ends
print('On an island'.strip('d'))    # ' On an islan' --> Strips all passed characters
                                    #                    from both ends
print('but life is good'.strip())   # ['but', 'life', 'is', 'good']

print('Help me'.replace('me', 'you'))    # 'Help you' --> Replace first with second
                                                   #                 parameter
print('Need to make fire'.startswith('Need'))      # True
print('and cook rice'.endswith('rice'))            # True
print('bye bye'.index('e'))                        # 2
print('still there?'.upper())                      # STILL THERE?
print('HELLO?!'.lower())                           # hello?!
print('ok, I am done.'.capitalize())               # 'Ok, I am done.'
print('oh hi there'.find('i'))                     # 4 --> returns the starting index position
                                                   #       of the first occurrence
print('oh hi there'.find('e'))                     # 2

#String Formatting

name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')                   # Hello there Andrei and Sunny
# Newer way to do things as of python 3.6
print('Hello there {} and {}'.format(name1, name2))  # Hello there Andrei and Sunny
print('Hello there %s and %s' % (name1, name2))            # # Hello there Andrei and Sunny
# you can also use %d, %f, %r for integers, floats, string representations
# of objects respectively

# Palindrome check

word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True

# Boolean

print(bool(True))
print(bool(False))

# all the below evaluate to False. Everything else will evaluate to True in Python

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

# List

my_list = [1, 2, '3', True]         # We assume this list won't mutate for each example below

print(len(my_list))                 # 4
print(my_list.index('3'))           # 2
print(my_list.count(2))             # 1 --> count how many times 2 appears

print(my_list[3])                   # True
print(my_list[1:])                  # [2, '3', True]
print(my_list[:1])                  # [1]
print(my_list[-1])                  # True
print(my_list[::1])                 # [1, 2, '3', True]
print(my_list[::-1])                # [True, '3', 2, 1]
print(my_list[0:3:2])               # [1, '3']

# : is called slicing and has the format [ start : end : step ]

# Add to list

print(my_list * 2)                              # [1, 2, '3', True, 1, 2, '3', True]
print(my_list + [100])                          # [1, 2, '3', True, 100]
# doesn't mutate original list, creates a new one
print(my_list.append(100))                      # None
# Mutates original list to [1, 2, '3', True, 100] or : <list> += [<el>]
print(my_list.extend([100, 200]))               # None
# Mutates original list to [1, 2, '3', True, 100, 200]
print(my_list.insert(2, '!!!'))    # None --> [1, 2, '!!!', '3', True]
# Inserts item at index and moves the rest to the right.

print(''.join(['Hello', 'There']))              # 'Hello There'
# Joins elements using string as separator.

# Copy a list

basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]
print(new_basket)
print(new_basket2)

# Remove from List

print([1,2,3].pop())         # 3 --> mutates original list, default index in the pop method is -1 (the last item)
print([1,2,3].pop(1))        # 2 --> mutates original list
print([1,2,3].remove(2))     # None --> [1,3] Removes first occurrence of item or raises ValueError.
print([1,2,3].clear())       # None --> mutates original list and removes all items: []
del [1,2,3][0]               #

# Ordering

print([1,2,5,3].sort())                 # None --> Mutates list to [1, 2, 3, 5]
print([1,2,5,3].sort(reverse=True))     # None --> Mutates list to [5, 3, 2, 1]
print([1,2,5,3].reverse())              # None --> Mutates list to [3, 5, 2, 1]
print(sorted([1,2,5,3]))                # [1, 2, 3, 5] --> new list created
print(list(reversed([1,2,5,3])))        # [3, 5, 2, 1] --> reversed() returns an iterator

# Useful operations

print(1 in [1,2,5,3])       # True
print(min([1,2,3,4,5]))     # 1
print(max([1,2,3,4,5]))     # 5
print(sum([1,2,3,4,5]))     # 15

# Get First and Last element of a list

mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first) #63
print(last) #10

# Read line of a file into a list

# with open("myfile.txt") as f:                 --> commented so no error "file not found  "
#     lines = [line.strip() for line in f]      --> commented so no error "file not found  "

# Dictionary

my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}
print(my_dict)

print(my_dict['name'])          # John Doe
print(len(my_dict))             # 3
print(list(my_dict.keys()))     # ['name', 'age', 'magic_power']
print(list(my_dict.values()))   # ['John Doe', 25, False]
print(list(my_dict.items()))    # [('name', 'John Doe'), ('age', 25), ('magic_power', False)]

my_dict['favourite_snack'] = 'Grapes' # {'name': 'John Doe', 'age': 25, 'magic_power': False, 'favourite_snack': 'Grapes'}
print(my_dict)

print(my_dict.get('age'))                    # 25 --> Returns None if key does not exist.
print(my_dict.get('ages', 0))    # 0 --> Returns default (2nd param) if key is not found

#Remove key

del my_dict['name']
print(my_dict)

my_dict.pop('name', None)
print(my_dict)

# Tuple

my_tuple = ('apple', 'grapes', 'mango', 'grapes')
print(my_tuple)

apple, grapes_1, mango, grapes_2 = my_tuple # Tuple unpacking
print(my_tuple)

print(len(my_tuple))                # 4
print(my_tuple[2])                  # mango
print(my_tuple[-1])                 # 'grapes'

# Immutability

# my_tuple[1] = 'donuts'            # TypeError
# my_tuple.append('candy')          # AttributeError

# Methods
print(my_tuple.index('grapes'))     # 1
print(my_tuple.count('grapes'))     # 2

# Set

my_set = set()
my_set.add(1)             # {1}
my_set.add(100)           # {1, 100}
my_set.add(100)           # {1, 100} --> no duplicates!
print(my_set)

new_list = [1,2,3,3,3,4,4,5,6,1]
set(new_list)             # {1, 2, 3, 4, 5, 6}
print(new_list)

my_set.remove(100)        # {1} --> Raises KeyError if element not found
print(my_set)
my_set.discard(100)
print(my_set)             # {1} --> Doesn't raise an error if element not found
my_set.clear()            # {}
print(my_set)
new_set = {1,2,3}.copy()  # {1,2,3}
print(my_set)

set1 = {1,2,3}
print(set1)
set2 = {3,4,5}
print(set2)

set3 = set1.union(set2)                 # {1,2,3,4,5}
print(set3)
set4 = set1.intersection(set2)          # {3}
print(set4)
set5 = set1.difference(set2)            # {1, 2}
print(set5)
set6 = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
print(set6)

print(set1.issubset(set2))      # False
print(set1.issuperset(set2))    # False
print(set1.isdisjoint(set2))    # False --> return True if two sets have a null intersection.

# Frozenset

# hashable --> it can be used as a key in a dictionary or as an element in a set.
# <frozenset> = frozenset(<collection>) --> Errors

# None

print(type(None))
a = None
print(a)






