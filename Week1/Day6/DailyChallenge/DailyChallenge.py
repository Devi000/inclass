# Instructions:
# Ask the user to enter a word.
# Store the input word in a variable.
# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.
#     * If it is, append the current index to the list associated with that key.
#     * If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
# 3. Expected Output:
# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.

word = input("Type any word: ")
char_indexes = {}
for index in range(len(word)):
    char = word[index]
    if char in char_indexes:
        char_indexes[char].append(index)
    else:
        char_indexes[char] = [index]
print(char_indexes)

# Instructions:
# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# You need to clean the dollar sign and the commas using python. Don’t hard code it.
# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.

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
