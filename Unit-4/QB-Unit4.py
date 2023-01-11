"""
1) Let a be the list of values produced by range(1, 11). Using the function filter and a lambda argument, write an expression that 
   will produce each of the following:
   a. A list of the even values in a
   b. A list of the values in a divisible by 3

2) Explain the following execution of the function filter. Hint: remember how integer values are interpreted when a Boolean is required.
>>> filter(lambda x: x, [4, 0, 6, 3, 0, 2])
    [4, 6, 3, 2]

Solution: Any number except 0 is treated as True in python.

Write a lambda function for each of the following:
a. Take one argument and return true if it is nonzero
b. Take one argument and return true if it is odd
c. Take two arguments, and return their sum
d. Take two arguments, and return true if their sum is odd
e. Take three arguments, and return true if the product of the 
   first two is less than or equal to the third


3) Let a be the list of values produced by range(1, 11). Using the function map and a lambda argument, write an expression 
that will produce each of the following:
a. A list of squares of the values
b. A list of cubes of the values
c. A list where each element is larger by one than the corresponding
   element in the original list

4) Write a function named returnSquares that returns as a function the squares of all the numbers of a list argument passed to it 
   in sorted order from lowest to highest. Your code must make use of list comprehensions.

5) Write a function named returnEvens that returns as a function value only the even numbers of a list argument passed to it. 
   Your code must make use of list comprehensions.

6) Give an appropriate list comprehension for each of the following.
   (a) Producing a list of consonants that appear in string variable w.
   (b) Producing a list of numbers between 1-100 that are divisible by 3.
   (c) Producing a list of numbers, zero_values, from a list of floating-point values, data_values, that are within some 
       distance, epsilon, from 0.

7) For the following function,

   def hours_of_daylight(month, year)

     a. Give an appropriate docstring specification where  hours_of_daylight returns the total number of hours of daylight for the 
         month and year given (each passed an integer value) designed so that the function does not check for invalid parameter values.
     b. Give a print statement that displays the docstring for this function.

8) Use a list comprehension print even numbers from 0 to n(n is some arbitrary value).

9) Using list comprehension print the Fibonacci Sequence in comma separated form for given input n.

10) Using list comprehension, write a program to print the list after removing the 0th, 2nd, 4th , 6th elements in [2,14,45,19,18,10,55].  

11) Using list comprehension, write a program to print the list with numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

12) Let a be the list of values produced by range(1,11). Write a list comprehension that will produce each of the following:
    a. The values in a that are less than or equal to 5
    b. The squares of the values in a
    c. The cubes of the values in a that are less than or equal to 5
    d. The squares of those values in a that are even

13) For the following module,
    # module driving_conversions
    
    def milesPerHr(km_speed): '''Returns miles per hour for kilometers per hour given in speed. '''
    def milesPerGal(KilometersPerLiter): '''Returns miles per gallon for provided kilometers per liter. '''

    a. Provide a main module that makes use of this module to prompt the user for the conversion desired, 
        and displays the converted result, using the import modulename form of import.
    b. Modify (a) above using the from modulename import identifier, identifier form of import.
    c. Modify (a) above using the from modulename import * form of import.
    d. Modify (a) above using the from modulename import identifier as new_identifier form of import.
    e. Describe the namespaces for the main modules of (a), (b), (c) and (d) above. 

14) Import module math , and use its functions to complete the following exercises:
    a. Write a single expression that rounds the value of -4.3 and then takes the absolute value of that result.
    b. Write an expression that takes the ceiling of sine of 34.5

15) Given a list of numbers, write a list comprehension that produces a copy of the list

16) Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.

17) Given a sentence, return the setence with all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.

18) Write a list comprehension statement to generate a list of all pairs of odd positive integer values less than 
    10 where the first value is less than the second value.
"""

# 1
a = [i for i in range(1,11)]
x = list(filter(lambda x : x % 2 == 0, a))
y = list(filter(lambda x : x % 3 == 0, a))
print(x,y)

# 2
a =  lambda x : x == 0
b = lambda x : x % 2 != 0
c = lambda x,y : x + y
d = lambda x,y : True if (x+y) % 2 != 0 else False
e = lambda x,y,z : True if x*y <= z else False
print(a(1),b(1),c(12,12),d(12,13),e(1,2,3))

# 3
f = list(map(lambda x : x**2, range(1,11)))
g = list(map(lambda x : x**3, range(1,11)))
h = list(map(lambda x : x+1, range(1,11)))
print(f,g,h)

# 4
l1 = [5,23,52,7,1,3,9,12,22]

def returnSquares(a):
    l2 = [i**2 for i in a]
    l2.sort()
    return l2

print(returnSquares(l1))

# 5
l3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def returnEvens(b):
    l4 = [i for i in b if i % 2 == 0]
    return l4

print(returnEvens(l3))

# 6
w = "hi welcome to the unit04 question bank solutions file"
vowels = ['a', 'e', 'i', 'o', 'u']
l = list(set([k for i in w.split() for k in i if k not in vowels]))      # better way to do this since the list would be huge with repeated values

div3 = [x for x in range(1,101) if x % 3 == 0]

data_values = [0.28,0.99,0.54,0.88,0.43,0.72]
epsilon = 0.6
zero_values = [i for i in data_values if i < epsilon]

print(l,div3,zero_values, sep= '\n')

# 7
def hours_of_daylight(month, year):
    '''
    Returns the number of hours of daylight received in the month
    It takes the total sunlight of the year and divides it among the months.
    sunlight = (total_in_year / 12)*month
    '''

print(hours_of_daylight.__doc__)

# 8
n = 40
evenNumbers = [x for x in range(1,n+1) if x % 2 == 0]
print(evenNumbers)

# 9
fibbonaci = [int((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5) for n in range(0,10)]
print(fibbonaci)

# 10 
l22 = [2,14,45,19,18,10,55]
new_list = [l22[x] for x in range(len(l22)) if x != 0 and x != 2 and x != 4 and  x != 6]
print(new_list)

# 11
div7 = [x for x in [12,24,35,70,88,120,155] if x % 5 == 0 and x % 7 == 0]
print(div7)

# 12
x1 = [x for x in range(1,11)]
less_than_or_equal5 = [i for i in x1 if i <= 5]

squares = [s**2 for s in x1 ]

cubes = [c**3 for c in less_than_or_equal5]

even_squares = [l**2 for l in x1 if l % 2 == 0]

print(x1,less_than_or_equal5,squares,cubes,even_squares)

# 13
if __name__ == '__main__':

    type_of_conversion = int(input('What type of conversion do you want 1) kmph -> mph OR 2) kmpl -> mpg (1/2): '))

    # a
    import driving_conversions
    if type_of_conversion == 1:
        print(driving_conversions.milesPerHr(25))
    else:
        print(driving_conversions.milesPerGal(25))

    # b
    if type_of_conversion == 1:
        from driving_conversions import milesPerHr
        print(milesPerHr(25))
    else:
        from driving_conversions import milesPerGal
        print(milesPerGal(25))

    # c 
    from driving_conversions import *
    if type_of_conversion == 1:
        print(milesPerHr(25))
    else:
        print(milesPerGal(25))
    
    # d
    if type_of_conversion == 1:
        from driving_conversions import milesPerHr as mph
        print(mph(25))
    else:
        from driving_conversions import milesPerGal as mpg
        print(mpg(25))

# 14
import math
print(abs(math.ceil(-4.3)))

# 15
numbers = [1,2,3,4,5,6,7,8,9]
copy = [x for x in numbers]
print(copy)

# 16
sentence = 'one of the greatest scientists to have existed was albert einstein he gave the theory of relativity!'
lengths = [len(word) for word in sentence.split() if word != 'the']
print(lengths)

# 17
x = list(map(lambda x: chr(ord(x)+1) if x != 'z' and x != ' ' and x != '!' else x , sentence))
new_sentence = ''
for i in x:
    new_sentence += i
print(new_sentence)

# 18
odds = [(x,x+2) for x in range(1,10)]
print(odds)

