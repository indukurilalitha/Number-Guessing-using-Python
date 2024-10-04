import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100. You have 10 attempts.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {number}.")

if __name__ == "__main__":
    number_guessing_game()
