# ------------------------------------------------------------------ # 
# Questions
# ------------------------------------------------------------------ # 

questions_easy = [
  "Easy Question 1: Is there any difference in \'a\' or \"a\" in python?\nTrue or False",
  "Easy Question 2: Index value of string can be in float\nTrue or False.",
  "Easy Question 3: Guido van Rosum created Python?\nTrue or False",
]

questions_hard = [
  """Hard Question 1: IF statement syntax is: 
  if < condition >;
    code
True or False?
  """,
  "Hard Question 2: The else statement executes only if the evaluation of the if and all the elif expressions are False\nTrue or False",
  """Hard Question 3:
a = 13
b = 18
c = 2
d = 20
if b > a and b != a and b <= c and d > b:
  print("True")
  Question: The output will have an error?
  """,
]

questions_vhard = [
  """Very Hard Question 1: 
  1) With the while loop we can execute a set of statements as long as a condition is true.
  2) With the break statement we can stop the loop even if the while condition is true.
  3) Continue statement is used to skip the rest of the code inside a loop for the current iteration only.  
  True or False?
  """,
  "Very Hard Question 2: The range() function can also modify it’s 3 defaults arguments. The first two will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.\nTrue or False",
  "Very Hard Question 3: You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.\nTrue or False",

]

# ------------------------------------------------------------------ # 
# Answers
# ------------------------------------------------------------------ # 

answers_easy = [
  "false",
  "false",
  "false", # Guido van Rossum
]

answers_hard = [
  "false",
  "true",
  "true",
]

answers_vhard = [
  "true",
  "true",
  "true",
]

# ------------------------------------------------------------------ # 

# Introduction
print("""This game is educational and would cover some topics related to software engineering.
You can choose difficulty of questions and answer by typing true or false.
""")

# Start game
start_game = input("""
Game Start?
y/n:
""")

if start_game == "n":
  exit()

# Variables
point = 0
playing = True

#Logic
while playing == True:
  # Choose Difficulty
  choose_lvl = input("""Choose difficulty: 
  Easy = 1 point
  Hard = 2 points
  Very Hard  = 3 points
  """)

  if choose_lvl.lower() == "easy":
    point = 0
    wrong = 0

    for i in range(len(questions_easy)):
      print(questions_easy[i])
      answer = input("Answer: ")

      if answer == answers_easy[i]:
        print("Correct")
        point+=1
      else:
        print("Wrong")
        wrong+=1

    
  # Difficulty = Hard
  if choose_lvl.lower() == "hard":
    point = 0
    wrong = 0
    for i in range(len(questions_hard)):
      print(questions_hard[i])
      answer = input("Answer: ")

      if answer == answers_hard[i]:
        print("Correct")
        point+=2
      else:
        print("Wrong")
        wrong+=1

  # Difficulty = Very Hard
  if choose_lvl.lower() == "very hard":
    point = 0
    wrong = 0
    for i in range(len(questions_vhard)):
      print(questions_vhard[i])
      answer = input("Answer: ")

      if answer == answers_vhard[i]:
        print("Correct")
        point+=3
      else:
        print("Wrong")
        wrong+=1

  #Exit loop
  exit_loop = input(f"""End of questions
  play again?
  y/n
  """)

  if exit_loop == "y":
    playing == True
    
  else:
    break

print(f"""Thank you for playing.
Score: {point}
Errors: {wrong}
""")
