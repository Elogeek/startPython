# Init lists
list_numbers = [1, 6, 98, 52, 1045, 3]
hobbies =["travel", "Japan+++", "walking in the nature", "food"]

# Sort the list in order
list_numbers.sort()
print(list_numbers)

# Delete the first item in the list_numbers
list_numbers.pop(0)

# Add a number at the end of list_numbers
list_numbers.append(5657)

# Collect the second item from the hobbies list
hobby = hobbies[1]
print(hobby)

# Add an item to the beginning of the hobbies list
hobbies.insert(0, "listen to music")
print(hobbies)

# Show hobby list length
print(len(hobbies))

# Init tuples (tuple is immutable (cannot be changed))
number_tuple = (1, 2, 5, 9)
print(number_tuple)

# init dictionary ( = associative array in PHP)
dico = {}
dico = {
    "name": "Elodie",
    "pseudo_dev": "Elogeek",
    "age": 30,
    "activity_favorite": ["travel", "Japan+++", "walking in the nature", "food", "listen to music"]
}

print(dico)

# Retrieve the name via the "name" key in the array
person = dico["name"]
print(person)

# Delete the "age" key from the dictionary
person_age = dico.pop("age")
print(dico)

# Retrieve the developer pseudo in the table
person_pseudo = dico["pseudo_dev"]
print(f"Le nom du dév est {person_pseudo}")

