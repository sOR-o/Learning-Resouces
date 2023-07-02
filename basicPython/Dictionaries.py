# Creating a dictionary
person = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

# Accessing values
print(person["name"])  # Output: John

# Modifying values
person["age"] = 30

# Adding new key-value pairs
person["occupation"] = "Engineer"

# Removing a key-value pair
del person["country"]

# Dictionary length
length = len(person)

# Printing dictionary
print(person, length)
