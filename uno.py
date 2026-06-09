import random

class Card:
  def __init__(self, color, value):
    self.color = color
    self.value = value

class Deck:
  def __init__ (self):
    self.card = []
    
  def shuffle(self):
    random.shuffle(self.card)

  def build_deck(self):
    color_set = ["Red", "Green", "Blue", "Yellow"]
    value_set = range(1,10)
    action_card = ["+2", "Skip", "Reverse"]
    wild_card = ["+4", "Wild"]

    for i in color_set:
      new_card = Card(i ,0)
      self.card.append(new_card)
    for _ in range(2):
      for i in color_set:
        for j in value_set:
          new_card = Card(i ,j)
          self.card.append(new_card)
    for _ in range(2):
      for i in color_set:
        for j in action_card:
          new_card = Card(i, j)
          self.card.append(new_card)
    for _ in range(4):
      for i in wild_card:
        new_card = Card("Black", i)
        self.card.append(new_card)

class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def draw(self, deck):
    drawn_card = deck.card.pop()
    self.hand.append(drawn_card)

player1 = Player("Rohan")
computer = Player("Computer")

my_uno = Deck()
my_uno.build_deck()
my_uno.shuffle()

for _ in range(7):
  player1.draw(my_uno)
  computer.draw(my_uno)

discard_pile = []
discard_pile.append(my_uno.card.pop(0))

game_over = False
curr_turn = "Player"
curr_card = discard_pile[0]

while not game_over:
  print(f"\nThe first Draw card is {curr_card.color}, {curr_card.value}")

  if curr_turn == "Player":
    for index,i in enumerate(player1.hand):
      print(f"{index} {i.color}, {i.value}")
    player_choice = input("Would you like to Draw(D) or Play(P): ").upper()
    if player_choice == "D":
      player1.draw(my_uno)
      drawn_card = player1.hand[-1] 
      print(f"You drew a: {drawn_card.color} {drawn_card.value}")
      if drawn_card.value == curr_card.value or drawn_card.color == curr_card.color or drawn_card.color == "Black":
        play_it = input("It's a match! Do you want to play it? (Y/N): ").upper()
        if play_it == "Y":
          played_card = player1.hand.pop()
          discard_pile.append(played_card)
          curr_card = played_card
          print("You played your drawn card!")

          if curr_card.color == "Black":
            curr_card.color = input("Choose a color (Red, Green, Blue, Yellow): ").capitalize()
            print(f"Color changed to {curr_card.color}!")

          if curr_card.value == "Skip" or curr_card.value == "Reverse":
            print("Turn skipped! You get to go again!")
          elif curr_card.value == "+2":
            print("Computer draws 2 cards! You go again!")
            for _ in range(2): 
              computer.draw(my_uno)
          elif curr_card.value == "+4":
            print("Computer draws 4 cards! You go again!")
            for _ in range(4): 
              computer.draw(my_uno)
          else:
            curr_turn = "Computer"
        else:
          curr_turn = "Computer" 
      else:
        curr_turn = "Computer" 
        
  
    else:
      card_index = int(input("Enter the card index from the given: "))
      chosen = player1.hand[card_index]
      if chosen.value ==curr_card.value or chosen.color == curr_card.color or chosen.color == "Black":
        print("Valid Move")
        played_card = player1.hand.pop(card_index)
        discard_pile.append(played_card)
        curr_card = played_card
        print(f"You played a {curr_card.color} {curr_card.value}!")
        if curr_card.color == "Black":
          curr_card.color = input("Choose a color (Red, Green, Blue, Yellow): ").capitalize()
          print(f"Color changed to {curr_card.color}!")
          
        if curr_card.value == "Skip" or curr_card.value == "Reverse":
            print("Turn skipped! You get to go again!")
        elif curr_card.value == "+2":
            print("Computer draws 2 cards! You go again!")
            for _ in range(2):
                computer.draw(my_uno)
        elif curr_card.value == "+4":
            print("Computer draws 4 cards! You go again!")
            for _ in range(4):
                computer.draw(my_uno)
        else:
            curr_turn = "Computer"
      else:
        print("Not possible!")
        
  if len(player1.hand) == 1:
    print(f"\n{player1.name}: UNO!")
  if len(player1.hand) == 0:
    print("\nUNO! You win!")
    game_over = True
            
  elif curr_turn == "Computer":
    has_played = False
    for index, card in enumerate(computer.hand):
      if card.value == curr_card.value or card.color == curr_card.color or card.color == "Black":
        played_card = computer.hand.pop(index)
        discard_pile.append(played_card)
        curr_card = played_card
        print(f"The Computer played a {curr_card.color} {curr_card.value}!")
        has_played = True

        if curr_card.color == "Black":
          curr_card.color = random.choice(["Red", "Green", "Blue", "Yellow"])
          print(f"The Computer changed the color to {curr_card.color}!")
          
        if curr_card.value == "Skip" or curr_card.value == "Reverse":
            print("The Computer goes again!")
            curr_turn = "Computer"
        elif curr_card.value == "+2":
            print("You draw 2 cards! Computer goes again!")
            for _ in range(2):
                player1.draw(my_uno)
            curr_turn = "Computer"
        elif curr_card.value == "+4":
            print("You draw 4 cards! Computer goes again!")
            for _ in range(4):
                player1.draw(my_uno)
            curr_turn = "Computer"
        else:
            curr_turn = "Player"
        break 

    if has_played == False:
      computer.draw(my_uno)
      drawn_card = computer.hand[-1]
      print("The Computer had no matches and drew a card.")

      if drawn_card.value == curr_card.value or drawn_card.color == curr_card.color or drawn_card.color == "Black":
        print(f"The Computer immediately played its drawn card: {drawn_card.color} {drawn_card.value}!")
        played_card = computer.hand.pop()
        discard_pile.append(played_card)
        curr_card = played_card
        
        if curr_card.color == "Black":
          curr_card.color = random.choice(["Red", "Green", "Blue", "Yellow"])
          print(f"The Computer changed the color to {curr_card.color}!")
          
        if curr_card.value == "Skip" or curr_card.value == "Reverse":
            print("The Computer goes again!")
            curr_turn = "Computer"
        elif curr_card.value == "+2":
            print("You draw 2 cards! Computer goes again!")
            for _ in range(2):
                player1.draw(my_uno)
            curr_turn = "Computer"
        elif curr_card.value == "+4":
            print("You draw 4 cards! Computer goes again!")
            for _ in range(4):
                player1.draw(my_uno)
            curr_turn = "Computer"
        else:
            curr_turn = "Player"
      else:
        curr_turn = "Player"
        
    if len(computer.hand) == 1:
      print("\nComputer: UNO!")
    if len(computer.hand) == 0:
      print("UNO! The Computer wins!")
      game_over = True