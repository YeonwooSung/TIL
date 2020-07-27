# 1. Swapping the value of 2 variables

# using temporal variable
a = 1
b = 2
temp = a
a = b
b = temp

# one liner method
a = 1
b = 2
a, b = b, a


# 2. List comprehension

# using for loop
ls = []
for i in range(5):
    ls.append(i)

# one liner method
ls = [i for i in range(5)]

# You can also add use list comprehension to iterate an existing list and provide some criteria that need to be fulfilled by the element.
ls = [-1, 2, -3, 6, -5]
ls = [i for i in ls if i > 0]  # ls = [2, 6], positive integers only


# 3. Map method

ls = list(map(int, ["1", "2", "3"])) #ls = [1, 2, 3]


# 4. Filter method

# The filter method in Python checks iterables, for example, the elements of a list and removes the elements that return False (do not meet the criteria). 
# In this example, we will take advantage of the filter method to find the common elements in two lists.

ls1 = [1, 3, 5, 7, 9]
ls2 = [0, 1, 2, 3, 4]
common = list(filter(lambda x: x in ls1, ls2)) #common = [1, 3]


# 5. Reduce method

# Reduce method in Python is used to apply a function to every element until only one element is left. 
# As the name suggests, the method reduces an array into a single element.

# Reduce function is defined in the “functools” modules, so don’t forget to import it beforehand!

from functools import reduce
print(reduce(lambda x, y: x*y, [1, 2, 3])) #print 6



# 6. Lambda function

def fullName(first, last):
    return f"{first} {last}"

name = fullName("Tom", "Walker")  # name = Tom Walker

# Lambda function is a small anonymous (one-line) function that is capable to substitute a regular function that is declared with the def keyword. 
# The above snippet is similar to this one.

fullName_oneliner = lambda first, last: f"{first} {last}"
name = fullName_oneliner("Tom", "Walker") #name = Tom Walker

# The power of lambda will be clearer when we use it as a higher-order function. 
# A higher-order function is a function which takes other function/functions as arguments or returns other function/functions.

highOrder = lambda x, func: x + func(x)
result1 = highOrder(5, lambda x: x*x) #result1 = 30
result2 = highOrder(3, lambda x : x*2) #result2 = 9

