import random


def deal_cards(n):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards, n)


def calculate_score(sequence):
    total = sum(sequence)
    if total == 21 and len(sequence) == 2:
        return 0
    if total > 21 and 11 in sequence:
        sequence.remove(11)
        sequence.append(1)
    return sum(sequence)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, Computer has a black jack"
    elif u_score ==0:
        return "You win, You have a BlackJack"
    elif u_score > 21:
        return "You lose"
    elif c_score > 21:
        return "You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play():
  user_cards = []
  computer_cards = []
  end_game = False
  
  user_cards.extend(deal_cards(2))
  computer_cards.extend(deal_cards(2))
  
  
  while not end_game:
  
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
  
      print(f"Your cards are: {user_cards}, your score is: {user_score}")
      print(f"Computer's first card is: {computer_cards[0]}")
  
      if user_score == 0 or computer_score == 0 or user_score > 21:
          end_game = True
      else:
          deal = input("Type 'y' to add another card, 'n' to pass: ")
          if deal == 'y':
              user_cards.extend(deal_cards(1))
          elif deal == 'n':
              end_game = True
  
  while computer_score != 0 and computer_score < 17:
      computer_cards.extend(deal_cards(1))
      computer_score = calculate_score(computer_cards)
  
  print(f"Your cards are: {user_cards}, your score is: {user_score}")
  print(f"Computer's first card is: {computer_cards}, computer score is: {computer_score}")
  print(compare(user_score, computer_score))
  

while input("\n\nDo you want to play? press Enter key to play, press any other key to end: ") == '':
  play()