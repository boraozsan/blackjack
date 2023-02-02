import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=[]
computer_cards=[]
end_game=False
def deal_card():
    random_card=random.choice(cards)
    return random_card

def calculate_score(cards):
    if len(cards)==2 and sum(cards)==21:
            return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def result(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You lose!"


  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "You Lose, opponent has Blackjack!"
  elif user_score == 0:
    return "You Win, you have Blackjack!"
  elif user_score > 21:
    return "You lose!"
  elif computer_score > 21:
    return "You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while end_game==False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards :{user_cards} Current Score :{user_score}")
    print(f"Computer's first card:{computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21 or user_score==21:
        end_game=True
    else:
        answer=input("Want u draw card? (y or n)")
        if answer =="y":
            user_cards.append(deal_card())
        else:
            end_game=True



    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(result(user_score, computer_score))
