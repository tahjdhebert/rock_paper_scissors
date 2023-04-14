import random

def play():
  in_computer = ["rock", "paper", "scissor"]
  print("Welcome to Rock, Paper, Scissors!")
  
  user_play = input("Choose your attacker (rock, paper, scissors): ")
  computer_play = "scissors"#random.choice(in_computer)

  print(f"You played {user_play}. I played {computer_play}.")

  if user_play.isalpha() and user_play.lower() in ["r", "rock", "p", "paper", "s", "scissors"]:
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

