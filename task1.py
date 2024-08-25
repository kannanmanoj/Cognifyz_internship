import random #built in package usually use in all numbers 

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Step 2: Define game rules and logic
# Randomly choose a number between 1 and 10
secret_number = random.randint(1, 10)

# Player has 5 attempts 
attempts = 5 #this is optional

# Step 3: Use conditional statements to manage game flow
while attempts > 0:
    # Prompt the player to guess the number
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        break  # Exit the loop since the player has guessed correctly
    
    attempts -= 1  # Decrease the number of attempts by 1
    
    if attempts > 0:
        print(f"You have {attempts} attempt(s) left.\n")# f denotes way to format strings 
    else:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}. Better luck next time!")

# Game over message
print("Game Over!")
