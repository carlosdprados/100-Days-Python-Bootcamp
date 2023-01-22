#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day 4 Project: Rock-Paper-Scissors
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Here you can try challenging the computer on a Rock-Paper-Scissors games.
You can play on Normal Mode, where you have a simple 33.33% of winning, losing, or drawing. Or:
Hard Mode, where an algorithm will give the computer more chance of winning (you will have around 20% of win probability).
The program will ask you to play again and will also record your Win Rate %. The computer will mock you if you give up.
You can also mess up: if you get the computer mad because of a misinput, you could have an unwinnable case(s).
The computer will also mock you if you give up.
Finally, if you repeat a choice multiple times, the computer will learn and win.
Good luck!
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_inputs = []
computer_inputs = []
number_games = 0
number_wins = 0
number_draw = 0
win_rate = 0
keep_playing = ''
keep_playing_flag = 1
difficulty = ''

#Introduction, difficulty settings, and welcoming
print("This is Rock-Paper-Scissors!")
difficulty = input("\nType Normal for playing Normal mode, or Hard for playing Hard mode: ").lower()
if difficulty == "normal":
    print ("You have made a good choice.\n")
elif difficulty == "hard":
    print ("Prepare to suffer.\n")
else:
    print("Don't try to make me mad. You'll regret it!")

while keep_playing_flag == 1:    
#Choosing user's option    
  human_choice = int(input("Type 1 for Rock, 2 for Paper, and 3 for Scissors: ")) - 1 #int and minus 1 to be compatible with index calling 
  if human_choice > 2 or human_choice < 0:
    print ("\nYou're pulling my hair, stop it! *breaks*\n")
    human_choice == int(0)
    difficulty == 'You asked for it.'
  
  if difficulty == "normal":
    computer_choice = random.randint(0,2)   #Plain 33% Draw, Win or Lose
  
  elif difficulty == "hard":    #Defining tricky computer algorithm
    if human_choice == 0:
      a = 1 / 3
      b = 0.8
    elif human_choice == 1:
      a = 0.2
      b = 0.2 + (1/3)
    else:
      a = 0.8 - (1/3)
      b = 2 / 3
    computer_dice = random.random()
    if computer_dice < a:
      computer_choice = 0
    elif computer_dice < b:
      computer_choice = 1
    else:
      computer_choice = 2
  else:   #Impossible game - Unwinnable
    if human_choice == 0:
      computer_choice = 1
    elif human_choice == 1:
      computer_choice = 2
    else:
      computer_choice = 0
  
  user_inputs.append(human_choice)
  if len(user_inputs)>3:
    if user_inputs[-3:].count(0) == 3:
      computer_choice = 1
    elif user_inputs[-3:].count(1) == 3:
      computer_choice = 2
    elif user_inputs[-3:].count(2) == 3:
      computer_choice = 0
    
  #Generating lists for easily calling different choice options and corresponding ASCII figures
  choices = [human_choice, computer_choice]
  shapes = [rock, paper, scissors] #defined in the beginning of the code as ASCII str figures
  shapes_names = ["Rock", "Paper", "Scissors"]
  
  #Showing visual effects of chosen options
  print("\nYou chose " + shapes_names[human_choice] + ":")
  print(shapes[human_choice])
  
  print("\nThe computer chose " + shapes_names[computer_choice] + ":")
  print(shapes[computer_choice])
  
  #Calculating winner
  if human_choice == computer_choice:
    print("It's a Draw!")
    number_draw += 1
  
  
  elif choices.count(0) == 0:
    if human_choice > computer_choice:
      print("Scissors beat Paper. You win!")
      number_wins += 1
    else:
      print("Scissors beat Paper. You lose!")
  
  else:
    if choices.count(1) == 1:
      if (human_choice - computer_choice) == 1: #could have used > but I liked this algorithm 
        print("Paper beats Rock. You win!")
        number_wins += 1
      else:
        print("Paper beats Rock. You lose!")
    else:
      if human_choice > computer_choice:
        print("Rock beats Scissors. You lose!")
      else:
        print("Rock beats Scissors. You win!")
        number_wins += 1
  number_games += 1 
  if number_games == number_draw:
    win_rate = float(50)
  else:
    win_rate = float(number_wins/(number_games-number_draw)*100)
  print(f"\nYou have played {number_games} times and your win rate is: {win_rate}%.\n")
  while True:
    try:
      keep_playing=input('Do you want to keep playing? Press Y/N').lower()
      break
    except ValueError:
      print("Please enter a valid response.\n")
  if keep_playing == "n" and win_rate <= 50:
    print("Giving up won't take you anywhere.\n\nGAME OVER")
    keep_playing_flag = 0
  elif keep_playing == "n" and win_rate > 50:
    print("Well done, sir. You managed to beat me. GGs.\n\nTHANK YOU FOR PLAYING!!")
    keep_playing_flag = 0
  elif keep_playing != "y" and win_rate <= 50:
    print("You had your chance to type a valid answer. Now get out of my sight.\n\nGAME OVER")
    keep_playing_flag = 0
  elif keep_playing != "y" and win_rate > 50:
    print("You had your chance to type a valid answer. Now get out of my sight.\n\nCongrats on beating me, BTW.")
    keep_playing_flag = 0
  else:
    print("Let's do it.\n")
