# 1. dict() constructor

# Create a dict object from tuples
dict_tuples = dict([("a", 0), ("b", 1), ("c", 2)])
print(dict_tuples)

# we could do same thing by using zip() function with 2 lists
dict_keys = ["a", "b", "c"]
dict_values = [0, 1, 2]
dict_zipped = dict(zip(dict_keys, dict_values))
print(dict_zipped)


# 2. Dictionary Comprehension

squares = {x: x*x for x in range(5)}


# 3. Retrieving Values

student = {"name": "John", "student_id": 73802}

name = student["name"] if "name" in student else "Unknown"
gender = student["gender"] if "gender" in student else "Unknown"

print('name = {}, gender = {}'.format(name, gender))


# 4. Iterations

currencies = {"America": "USD", "China": "CNY", "Britain": "GBP"}

# iteration over keys
for item in currencies:
    print(item)

# iteration over keys
for item in currencies.keys():
    print(item)

# iteration over values
for item in currencies.values():
    print(item)

# iteration over items
for key, value in currencies.items():
    print(f"Key: {key}; Value: {value}")


# 5. Merging Dictionaries

# The first merging method is Dictionary.update()
d0 = {"a": 0, "b": 1}
d1 = {"b": 2, "c": 3}
d0.update(d1)
print(d0)

# The second method is to use double asterisks (**) to unpack the dictionary.
d0 = {"a": 0, "b": 1}
d1 = {"b": 2, "c": 3}
d2 = {**dict0, **dict1}
print(d2)

# The third method is to use the dict() constructor, 
# which can take a dictionary and unpacked key-value pairs of the other dictionary.
d0 = {"a": 0, "b": 1}
d1 = {"b": 2, "c": 3}
d2 = dict(d0, **d1)
print(d2)
