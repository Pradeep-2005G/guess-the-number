import random
def guess_number():
    number_to_guess = random.randint(1, 50)
    guess = None
    attempts = 0
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1
        if guess < number_to_guess:
            print("SAY HIGH NUMBER!")
        elif guess > number_to_guess:
            print("SAY LOW NUMBER!")
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
guess_number()

