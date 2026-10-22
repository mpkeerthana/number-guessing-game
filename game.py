import random

def print_rules():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Your task is to guess the number.")
    print("After each guess, I will tell you if your guess is too high, too low, or correct.")
    print("You have unlimited attempts to guess the number. Good luck!")

def generate_number():
    return random.randint(1,100)

def play_game():
    number=generate_number()
    attempts=0
    max_attempts=7

    print_rules()

    while attempts<max_attempts:
        try:
            guess=int(input("Enter your gues(1-100): "))

            if guess<1 or guess>100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts+=1

            if guess<number:
                print("Your guess is too low. Try again.")  

            elif guess>number:
                print("Your guess is too high. Try again.") 

            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                return
            print("Attempt's left:", max_attempts-attempts)

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts==max_attempts and guess!=number:
        print(f"Sorry, you've used all your attempts. The correct number was {number}. Better luck next time!")

play_game()