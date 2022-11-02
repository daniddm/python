
import random



def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare (user_score, computer_score):
  if user_score == computer_score:
    return "Draw :)"
  elif computer_score == 0:
    return "lose the game!!!"
  elif user_score == 0 :
    return "win  the game!!!"
  elif user_score > 21 :
    return "lose user >21  the game!!!"
  elif computer_score > 21 :
    return "lose computer > 21  the game!!!"
  elif user_score > computer_score :
    return "you win!!!"
  else:
    return "you lose"


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
    else:
        user_shoul_deal = input("Type 'yes' to get another card, type 'no' to pass: ")
        if user_shoul_deal == "yes":
          user_cards.append(deal_card())
        else:
          is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
      
  print(f'your final hand : {user_cards} and the final score is {user_score}')
  print(f'the computer final hand : {computer_cards} and the final score is {computer_score}')
  print(compare(user_score, computer_score))

while input("do you want to play a game of Blackjack? Type 'y' or 'n' : ") == "y":
   play_game()

