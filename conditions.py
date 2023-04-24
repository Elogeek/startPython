# Exo buying a television
wallet = 3000
television_price = 1500

# The price of television is less than 1000€
if 1000 < television_price <= wallet:
    wallet -= television_price
    print("Le prix de la télévision est bien inférieure à 1000€, l'achat est possible")
else:
    print("Le prix est supérieur à 1000€, l'achat est impossible, vous n'avez que {}€".format(wallet))

# Condition ternary
purchase = ("L'achat est possible", "L'achat est impossible") [television_price <= 1000]
print(purchase)
# Show wallet after purchase
print(wallet)

# Exo password verification system
password = input("Entrer votre mot de passe, svp")
password_length = len(password)

# Check if the password is less than 5 characters
if password_length <= 5:
    print("Mot de passe trop court!")
elif password_length > 5 and password_length <= 8:
    print("Mot de passe moyen!")
else:
    print("Mot de passe super!")
print(password_length)

# Exo travel in Japan
person_age = int(input("Quel est votre âge?"))

# So minor
if person_age < 18:
    total_trip_price = 7
    print("Votre billet d'avion est de 7 euros")
else:
    total_trip_price = 15
    print("Votre billet d'avion est de 15 euros")

# If the person wants to travel in a kimono
kimono_travel_request = input("Voulez vous voyager en kimono? (oui, non)")

if kimono_travel_request == "oui":
    total_trip_price += 5

# Show total trip price
print("Votre voyage vous coûtera au total", total_trip_price, "€")