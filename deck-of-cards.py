# Write a program to shuffle Deck of cards.

import random

cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])

for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + " of " + suits[k])
        deck.append(card)

random.shuffle(deck)

for m in range(52):
    print(deck[m])
    
# ========= OR ==========
import itertools
import random

deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
random.shuffle(deck)

print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
