import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


number = random.randint(1,100)

def set_difficulty():
    """Chooses difficulty level and returns no. of turns"""
    level = input("Choose difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guessed_ans, correct_ans, turn):
    """Compares actual answer and guesses answer and returns no of turns remaining"""
    if guessed_ans == correct_ans:
        print(f"You Got it! The answer was {number}.")
        return
    elif guessed_ans > correct_ans:
        print("Too High.")
        print("Guess again.")
        return turn - 1
    else:
        print("Too Low.")
        print("Guess again.")
        return turn - 1


def game():
    print(logo)
    print("Wellcome to the Number Guessing Game.")
    print("I am thinking a number between 1 and 100.")
    turns = set_difficulty()
    guess = 0
    print("anderr", number)
    while guess != number:

        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)

        if turns == 0:
            print("You have run out of guesses. You Lose!")
            return

game()
