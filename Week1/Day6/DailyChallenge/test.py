

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
clean_wallet = int(wallet.replace("$", "").replace(",", ""))

print(type(clean_wallet))

basket = []
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= clean_wallet:
        basket.append(item)
        clean_wallet -= clean_price
print(basket)