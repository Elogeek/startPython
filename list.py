import statistics
# Import shuffle
from random import shuffle

notes = [
    5, 12, 8,
    10, 2, 20,
    2, 6, 9,
]
shuffle(notes)
print(notes)
# module statistics
result = statistics.mean(notes)
print("La moyenne de l'élève est de {}".format(result))

# Exo sentence generator
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")

# Turn this string into a list then mix it
words = chained_words.split("/")
shuffle(words)

# Get the number of elements
words_len = len(words)

# If the number of elements in this list is less than 5, display the first two words
if words_len < 5:
    print(words[0], words[1])
# If the number of elements is greater than or equal to 5 show last 3
else:
    print(words[words_len - 1], words[words_len - 2], words[words_len - 3])

# Exo les boucles

# boucle for
for manga_number in range(1,5):
    print("Vous venez de lire votre manga n°",manga_number)
