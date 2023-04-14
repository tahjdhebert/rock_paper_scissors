"""
X TODO: senario: user ROCK X
X TODO: senario: user PAPER X
TODO: senario: user SCISSORS
TODO: senario: user INVALID
QUESTION: Keeping score across multiple games
"""

import random

def play():
  in_computer = ["rock", "paper", "scissor"]
  print("Welcome to Rock, Paper, Scissors!")

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


        
