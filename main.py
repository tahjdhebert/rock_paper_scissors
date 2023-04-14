"""
X TODO: senario: user ROCK X
X TODO: senario: user PAPER X
TODO: senario: user SCISSORS
TODO: senario: user INVALID
QUESTION: Keeping score across multiple games
"""

import random

def main():
  print("Welcome to Rock, Paper, Scissors!")
  
  computer_wins = 0
  user_wins = 0
  ties = 0
  
  on = True
  while on == True:
    result = play()
    if result == None:
      ties += 1

    elif result == True:
      user_wins += 1

    else:
      computer_wins += 1
      
    play_again = input("Do you want to play again?: ")

    if play_again in ["yes", "y"]:
      on = True

    else:
      on = False

  if computer_wins > user_wins:
    print("I won this tournament!")

  elif user_wins > computer_wins:
    print("You won this tournament!")

  else:
    print("We tied this tournament!")


def play():
  in_computer = ["rock", "paper", "scissors"]

  user_play = input("Choose your attacker (rock, paper, scissors): ")
  computer_play = random.choice(in_computer)

  print(f"You played {user_play}. I played {computer_play}.")

  if user_play.isalpha() and user_play.lower() in [
      "r", "rock", "p", "paper", "s", "scissors"
  ]:
    # logic for all cases where user plays rock
    if user_play.lower() in ["r", "rock"]:

      if computer_play == "rock":
        print("It's a tie!")
        return None
      elif computer_play == "scissors":
        print("You Win!")
        return True
      else:
        print("I Win!")
        return False

    # logic for all cases where user plays scissors
    elif user_play.lower() in ["s", "scissors"]:
      if computer_play == "rock":
        print("I win!")
        return False
      elif computer_play == "scissors":
        print("It's a tie!")
        return None
      else:
        print("You win!")
        return True

    # logic for all cases where user plays paper
    else:
      if computer_play == "rock":
        print("You win!")
        return True
      elif computer_play == "scissors":
        print("I win!")
        return False
      else:
        print("It's a tie!")
        return None

main()

        
