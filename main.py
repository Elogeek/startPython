# Init lists
list_numbers = [1, 6, 98, 52, 1045, 3]
hobbies =["travel", "Japan+++", "walking in the nature", "food"]

# classez la liste
list_numbers.sort()
# supprimer le premier élément de la liste
list_numbers.pop(0)
# ajouter un nombre à la fin de la list_numbers
list_numbers.append(5657)
# récupérez le deuxième élément de la liste hobbies
hobby = hobbies[1]
print(hobby)

# affichez la longueur de la liste
print(len(list_numbers))

# Init tuples
# warning tuple is immuables (ne peuvent pas être modifiés)
number_tuple = (1, 2, 5, 9)

# init dictionnaire ( = tableau associatif in PHP)
dico = {}
dico = {
    "name": "Elodie",
    "pseudo_dev": "Elogeek",
    "age": 30,
    "activity_favorite": ["travel", "Japan+++", "walking in the nature", "food", "listen to music"]
}

print(dico)

# Récupérer le nom via la key "name"
person = dico["name"]
print(person)

# Supprimez la key "age" du dictionnaire
person_age = dico.pop("age")
print(dico)

# Récupérez le nom du développeur
person_pseudo = dico["pseudo_dev"]
print(f"Le nom du dév est {person_pseudo}")

