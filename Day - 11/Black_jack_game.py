import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a List of cards and returns the score"""
    if sum(cards) == 21 and len(cards) ==2 :
        return 0
    if sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(c_score, u_score):
    if c_score == u_score:
        return "Draw"
    elif c_score == 0 :
        return "Lose ! Opponent has BlackJack"
    elif u_score == 0 :
        return "Win with a Blackjack !"
    elif u_score > 21:
        return "Lose, You went over."
    elif c_score > 21:
        return "You Win, Opponent went over."
    elif u_score > c_score :
        return "You Win"
    else:
        return "You Lose."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards : {user_cards}, Current Score : {user_score}")
        print(f"Computer's First Card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, 'n' to pass:") == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand : {user_cards}, Final Score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, Final Score : {computer_score}")
    print(compare(computer_score, user_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n' :"):
    print("\n"*20)
    play_game()
