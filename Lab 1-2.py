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

age = input("How old are you? ")
age = int(age)
pi = input("What is the value of pi? ")
pi = float(pi)

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

# all of the below evaluate to False. Everything else will evaluate to True in Python

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







