# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {5, 7, 28}
my_fav_numbers.add(67)
my_fav_numbers.add(69)
my_fav_numbers.remove(69)

friend_fav_numbers = {10, 3, 2}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. 
# Think about why you can’t add more integers to a tuple.

tuple_test = (1, 2 ,3 ,4 ,5)
tuple_test.append(6)

# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
appplehm = basket.count("Apples")
basket.clear()
print(basket)

# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

mixto = []
for i in range(1, 6):
    mixto.append(i + 0.5)
    mixto.append(i)
print(mixto)

# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for num in range(1, 21):
    print(num)

for par in range(1, 21):
    if par % 2 == 0:
        print(par)

# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
while True:
    username = input("Enter your name: ")
    if username.isdigit() or len(username) < 3:
        print("Please enter a name with at least 3 letters and no digits.")
    else:
        print("thank you")
        break

# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fav_fruits = input("Enter your favorite fruits, separated by spaces: ").split()
user_fruit = input("Enter the name of any fruit: ")
if user_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.5

while True: 
    topping = input("Enter a pizza topping ('quit' to finish): ")
    if topping.upper() == 'QUIT':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")      

total = base_price + (len(toppings) * topping_price)
print(f"Your toppings: {', '.join(toppings)} and it costs ${total}")

# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
fam_count = int(input("How many tickets would you like yo buy?: "))
for i in range(fam_count):
    age = int(input(f"Enter the age of ticket #{i + 1}: "))
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"The ticket price for ticker #{i + 1} is: ${price}")
    total_cost += price
print(f"The total cost for all tickets is: ${total_cost}")