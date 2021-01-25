############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import *
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hand_value(hand):
  """ compute the value of a hand in list form - if an 11 is in there and the total is over 21, subtract 10 """
  count = 0
  for card in hand:
    count += card
# if we are over 21, need to check aces value
  if count > 21:
#check how many aces we have
    num_aces = hand.count(11)
    while num_aces > 0 and count > 21:
      # subtract 10 for each ace if we are over 21
      count -= 10
      num_aces -= 1
  return count

def is_blackjack(hand):
  """ Check if a hand is blackjack """
  if hand.count(11) == 1 and hand.count(10) == 1 and len(hand) == 2:
    return True
  else:
    return False
def deal():
  """ deal a card, since the deck is infinite we can simplify and just randomly choose a value """
  card_value_index = random.randint(0, 12)
  return cards[card_value_index]


def play_a_hand():
  """ Main routine to play one hand """
  player_hand = []
  dealer_hand = []
  # Deal each player two cards
  player_hand.append(deal())
  player_hand.append(deal())
  dealer_hand.append(deal())
  dealer_hand.append(deal())
  stay = True
  while hand_value(player_hand) < 21 and stay:
    print(f"Players hand is: {player_hand}, count is {hand_value(player_hand)}")
    print(f"Dealer's first card is: {dealer_hand[0]}")
    hit_or_stay = input("Type 'y' for another card, 'n' to stay:")
    if hit_or_stay == 'n':
      stay = False
    else:
      player_hand.append(deal())
  player_Blackjack = is_blackjack(player_hand)
  dealer_Blackjack = is_blackjack(dealer_hand)
  player_count = hand_value(player_hand)
  if player_Blackjack:
      if dealer_Blackjack:
        print("You both have blackjack! Dealer wins!")
      else:
        print("Blackjack!")
  while hand_value(dealer_hand) < 17:
    dealer_hand.append(deal())
  dealer_count = hand_value(dealer_hand)
  print(f"Players hand is: {player_hand}, count is {player_count}")
  print(f"Dealer's hand is: {dealer_hand}, count is {dealer_count}")
  if player_count > 21:
    print("You went over 21! You lose...")
  elif player_count > dealer_count or (player_Blackjack and not dealer_Blackjack) or dealer_count > 21:
    print ("You win!")
  elif player_count == dealer_count:
    print("You  tied.")
  else:
    print ("You lose..")


keep_playing = True
while keep_playing:
  clear()
  print(logo)
  play_a_hand()
  if input("Do you want to play another hand? Type 'y' for another hand, anything else to quit. ") != 'y':
    keep_playing = False