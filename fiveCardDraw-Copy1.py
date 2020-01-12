from random import randint

cards = {1 : "Ace of Hearts",
         2 : "Two of Hearts",
         3 : "Three of Hearts",
         4 : "Four of Hearts",
         5 : "Five of Hearts",
         6 : "Six of Hearts",
         7 : "Seven of Hearts",
         8 : "Eight of Hearts",
         9 : "Nine of Hearts",
         10 : "Ten of Hearts",
         11 : "Jack of Hearts",
         12 : "Queen of Hearts",
         13 : "King of Hearts",
         14 : "Ace of Diamonds",
         15 : "Two of Diamonds",
         16 : "Three of Diamonds",
         17 : "Four of Diamonds",
         18 : "Five of Diamonds",
         19 : "Six of Diamonds",
         20 : "Seven of Diamonds",
         21 : "Eight of Diamonds",
         22 : "Nine of Diamonds",
         23 : "Ten of Diamonds",
         24 : "Jack of Diamonds",
         25 : "Queen of Diamonds",
         26 : "King of Diamonds",
         27 : "Ace of Clubs",
         28 : "Two of Clubs",
         29 : "Three of Clubs",
         30 : "Four of Clubs",
         31 : "Five of Clubs",
         32 : "Six of Clubs",
         33 : "Seven of Clubs",
         34 : "Eight of Clubs",
         35 : "Nine of Clubs",
         36 : "Ten of Clubs",
         37 : "Jack of Clubs",
         38 : "Queen of Clubs",
         39 : "King of Clubs",
         40 : "Ace of Spades",
         41 : "Two of Spades",
         42 : "Three of Spades",
         43 : "Four of Spades",
         44 : "Five of Spades",
         45 : "Six of Spades",
         46 : "Seven of Spades",
         47 : "Eight of Spades",
         48 : "Nine of Spades",
         49 : "Ten of Spades",
         50 : "Jack of Spades",
         51 : "Queen of Spades",
         52 : "King of Spades"
}

def five_card_draw(card):
  already_drawn = []
  first_card = randint(1, 52)
  already_drawn.append(first_card)
  second_card = randint(1,52)
  
  while second_card in already_drawn:
    second_card = randint(1,52)
  already_drawn.append(second_card)
  third_card = randint(1, 52)
  
  while third_card in already_drawn:
    third_card = randint(1, 52)
  already_drawn.append(third_card)
  fourth_card = randint(1, 52)
  
  while fourth_card in already_drawn:
    fourth_card = randint(1, 52)
  already_drawn.append(fourth_card)
  fifth_card = randint(1, 52)
  
  while fifth_card in already_drawn:
    fifth_card = randint(1, 52)
  already_drawn.append(fifth_card)
  return already_drawn

your_hand = five_card_draw(cards)

for i in your_hand:
  print(cards[i])
