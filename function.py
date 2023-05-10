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