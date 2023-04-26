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

# Boucle for
for manga_number in range(1,5):
    print("Vous venez de lire votre manga n°",manga_number)

users = ["blabla@gmail.com", "user@gmail.com", "user_two@yahoo.fr","truc@gmail.be","sakura@nihon.fr", "ceci_est_un_email.com"]
blacklist = ["truc@gmail.be","ceci_est_un_email.com"]

# j'envoie une newsletter à chaque utilisateur, j'affiche "newsletter envoyée" ou non
for user in users:

    if user in blacklist:
        print("Newsletter non envoyée, l'adresse mail: ", user, ' n\'est pas valide!')

    print("Newsletter envoyée à: ", user )

# boucle while

# savings for the vacancies/mois
savings_account = 100

while savings_account < 2000:
    # ajouter surplus
    savings_account +=50
    # afficher le résultat
    print("votre épagne actuelle est de : ", savings_account,  "€")

print("Youpi, c'est les vacances!")