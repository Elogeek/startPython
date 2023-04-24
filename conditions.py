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