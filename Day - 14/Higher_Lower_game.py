#Use random module to choose random Celebrity from the data.
# Compare A : name, a description, from country
# VS
# Compare B : name, a description, from country
# Input who has more followers? Type 'A' or 'B':
# Compare the followers of A and B
# Initialize variable score = 0
# If true : A = B and B = random and score =+ 1
# Switch accounts A = B, after correct answers
# If False : Sorry, that's wrong. Final score: 0

import random
import art
from game_data import data

A = random.choice(data)
B = random.choice(data)
score = 0

def compare_followers(a,b):
    if a['follower_count'] > b['follower_count']:

        return 'A'
    else:
        return 'B'

print(art.logo)

while True:

    print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B : {B['name']}, a {B['description']}, from {B['country']}")
    greater = compare_followers(A, B)
    print("Greater: ", greater)
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if greater == answer :
        print("\n" * 20)
        print(art.logo)
        score += 1
        print(f"You are right! current score : {score}.")

        A = B
        B = random.choice(data)
        if A == B:
            B = random.choice(data)

    else :
        print(f"Sorry, that's wrong. Final score: {score}")
        break
