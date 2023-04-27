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
# Module statistics
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

# Exercise the loops

# For loop
for manga_number in range(1,5):
    print("Vous venez de lire votre manga n°",manga_number)

users = ["blabla@gmail.com", "user@gmail.com", "user_two@yahoo.fr","truc@gmail.be","sakura@nihon.fr", "ceci_est_un_email.com"]
blacklist = ["truc@gmail.be","ceci_est_un_email.com"]

# I send a newsletter to each user, I display "newsletter sent" or not
for user in users:

    if user in blacklist:
        print("Newsletter non envoyée, l'adresse mail: ", user, ' n\'est pas valide!')

    print("Newsletter envoyée à: ", user )

# While loop

# savings for the vacancies/mois
savings_account = 100

while savings_account < 2000:
    # Add surplus
    savings_account +=50
    # Show result
    print("votre épagne actuelle est de : ", savings_account,  "€")

print("Youpi, c'est les vacances!")

# j'ai 200 recettes sur youtube
recipes_count = 2500

# audiance 10% de plus par mois après 2 ans
months = 0

# estimation de l'audiance des recettes
while months <= 24:
    # augmente l'audience
    recipes_count *= 1.10
    # afficher combien de fois les recettes on été visionnées
    print("Vos recettes ont été vu actuellement {} par vos abonnées".format(recipes_count))
    # passe au mois suivant
    months += 1