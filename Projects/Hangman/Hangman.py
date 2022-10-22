# imports 
from random import choice
import time

# intro 
print("hi")
time.sleep(1)
print("Welcome to my first game, Hangman!")
time.sleep(1)
print("This game is about guessing a random word about the theme by asking the user a letter for each word.")
time.sleep(1)
print("The theme will be countries.")
time.sleep(1)
print("This game has a limited number of guesses and a limited time of 30 seconds.")
time.sleep(1)
start_game = input("Start Game?\ny/n: ")

#logic
#Initialize
words = ["Japan", "Philippines", "China", "Bangladesh", "Singapore", "Taiwan", "Qatar"]
word = choice(words)

# max number of guesses per user
guess_limit = 7
guess_container = []
success = False
time_limit = 30
    
# set timer
if start_game == "y":
  start_time = int(time.time())
else:
  exit()

while not success:
  #time duration
  cur_time = int(time.time())
  duration = cur_time - start_time

  if duration >= time_limit:
    print("You ran out of time")
    break
  else:
    print(f"Remaining Time: {time_limit - duration} seconds")

  # display the current guessed words
  for letter in word: 
    if letter.lower() in guess_container:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("")

  #ask user for input
  player_input = input(f"Guess remaining:{guess_limit}\nGuess: ")

  #store inputs to container
  guess_container.append(player_input.lower())

  #user errors
  if player_input.lower() not in word.lower():
    guess_limit -= 1
    if guess_limit == 0:
      break
  
  # check if continue loop
  # exit
  success = True

  #Continue loop
  for letter in word:
    if letter.lower() not in guess_container:
      success = False

  
if success:
  print(f"You win! The word is {word}")
else:
  print(f"Game Over! The word is {word}\nThank you for playing!")
