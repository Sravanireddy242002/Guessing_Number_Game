import random
def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts!")
            guessed = True
        # Provide hints
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guess_number()
