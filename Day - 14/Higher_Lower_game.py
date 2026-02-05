#Use random module to choose random Celebrity from the data.
# Compare A : name, a description, from country
# VS
# Compare B : name, a description, from country
# Input who has more followers? Type 'A' or 'B':
# Compare the followers of A and B
# Initialize variable score = 0
# If true : A = B and B = random and score =+ 1
# If False : Sorry, that's wrong. Final score: 0

import random
from lib2to3.fixer_util import String

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
game_is_over = 1
while game_is_over != 0:
    print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']}")
    print(f"Compare A : {B['name']}, a {B['description']}, from {B['country']}")
    greater = compare_followers(A, B)
    print("Greater: ", greater)
    answer = String(input("Who has more followers? Type 'A' or 'B': "))

    if greater == answer :
        A = greater
        score += 1
        B = random.choice(data)
    else :
        print(f"Sorry, that's wrong. Final score: {score}")
        break



# if A == B:
#     print(True)
# else:
#     print(False)
