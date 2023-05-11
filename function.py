# Init function
def hi():
    print("Hello and welcome here!")
    result = 3 + 2
    print("La réponse est ", result)

hi()

def next_year():
    global year
    print("C'est la fin de l' année ", year)
    year += 1
    print("Début de l' année ", year)

year = 2020
next_year()

# Create a function that returns the highest result between a and b
def max_number(a,b):
    if a < b:
        return a
    else:
        return b

# Value a (first number)
number_a = int(input("Entrer un nombre"))
# Value b (second number)
number_b = int(input("Entrer un deuxième nombre"))
max_value = max(number_a, number_b)
# Result
print("La plus grosse valeur est ",max_value )