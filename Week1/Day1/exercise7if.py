# Ask the user for a number between 1 and 100
# If the number is a divisible by three, print Fizz
# If the number is a divisible by five, print Buzz.
# If the number is a divisible by both three and five, print FizzBuzz instead.

usernumber = int(input("ingresa numero: "))
if usernumber % 3 == 0 and usernumber % 5 == 0:
    print("FizzBuzz")
elif usernumber % 5 == 0:
    print("Buzz")
elif usernumber % 3 == 0:
    print("Fizz")