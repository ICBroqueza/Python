#import
from time import sleep, time

# Intro
print("""Welcome! This is game is based on the hand-clapping game inspired by traditional Filipino game called "Nanay Tatay". 

They are split into pairs with each pair facing each other. Members from both pairs face the center (the two pairs are perpendicular to each other). Each pair then does a hand clapping "routine" while singing. 

Routine is the number of times the hand must be clapped. 

Routine starts at 1 and after each round, routine will be incremented by 1. 

Conditions: 
1) In this game, user hand clapping will be implemented by pressing space bar then enter correctly. 
2) Like the game, user must be quick on pressing the spacebar for it has a time limit every chants.
3) Player must input the number of "Routines" he/she wants. 
""")

# Start game
start_game = input("Game start? \ny/n\n")
if start_game == "y":
  input_routine = int(input("Routine/s: "))
else:
  exit()

playing = True

#logic
while playing == True:
  
  for i in range(input_routine):
    # 1st routine
    start_time = time()
    print("Nanay,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break
    
    # 2nd routine
    start_time = time()
    print("Tatay,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 3rd routine
    start_time = time()
    print("Gusto ko tinapay,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 4th routine
    start_time = time()
    print("Ate,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 5th routine
    start_time = time()
    print("Kuya,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 6th routine
    start_time = time()
    print("Gusto ko kape,")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 6th routine
    start_time = time()
    print("Lahat ng gusto ko ay susundin niyo.")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

    # 7th routine
    start_time = time()
    print("Ang magkamali ay pipingutin ko.")
    player_input = input("")
    end_time = time()
    duration = end_time - start_time

    if duration >= 2:
      print("Too Slow, You lose!")
      break
    if len(player_input) != i + 1:
      print("You clapped wrong! You lose!")
      break

  #Exit loop
  exit_loop = input(f"""End of game
  play again?
  y/n
  """)

  if exit_loop == "y":
    playing == True
  else:
    break