# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("Player 1 got:")
for i in range(9):
 		print(deck[i][0], "of", deck[i][1])

print("Player 2 got:")
for i in range(10,18):
   print(deck[i][0], "of", deck[i][1])

print("Player 3 got")
for i in range(19,28):
		print(deck[i][0], "of" ,deck[i][1])

print("Player 4 got")
for i in range(29,37):
	print(deck[i][0], "of" ,deck[i][1])

