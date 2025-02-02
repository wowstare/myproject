a = 10
b = 8
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a ** b) # Exponentiation (10^3)
print(a % b)  # Modulo (remainder of 10 / 3)
length = 5
width = 3
area = length * width
print("The area is:", area)
age = 10
if age >= 10:
    print("You are 10 or Older!")
else:
    print("You are younger than 10.")

    number = float(input("Enter a number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
        for i in range(5):
            print("Hello!", i)
            for i in range(1, 11):
                print(i)
                import random

                secret_number = random.randint(1, 10)
                guess = int(input("Guess a number between 1 and 10: "))

                if guess == secret_number:
                    print("You win!")
                else:
                    print("You lose! The number was", secret_number)