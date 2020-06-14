
# For loop with enumerate

employees = ['John', 'Danny', 'Jennifer']
for id_number, name in enumerate(employees, start=30001):
    print("{}'s employee ID #: {}".format(str(id_number), name))


# reversed() function

meals = ['pizza', 'hamberger', 'pasta', 'ramen', 'salad']
for meal in reversed(meals):
    print(meal)


# sorted() function

unsorted_integers = [1, 4, 2, 6, 3, 9, 11]
# by using lambda, you could use the attribute of object as a key for thye sorted() function
for integer in sorted(unsorted_integers, key=lambda x: x, reverse=True):
    print(integer)


# zip() function
numbers0 = [4, 5, 6]
numbers1 = [11, 12, 13]
for j, k in zip(numbers0, numbers1):
    print('{} * k = {}'.format(str(j), str(k), str(j * k)))
