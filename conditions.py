wallet = 3000
television_price = 1500

# The price of television is less than 1000€
if television_price > 1000 and television_price <= wallet:
    wallet -= television_price
    print("Le prix de la télévision est bien inférieure à 1000€, l'achat est possible")
else:
    print("Le prix est supérieur à 1000€, l'achat est impossible, vous n'avez que {}€".format(wallet))

# Show wallet after purchase
print(wallet)