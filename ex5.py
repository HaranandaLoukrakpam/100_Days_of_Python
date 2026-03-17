# # to create a snake water gun game similar to rock paper scissor using if else statement 
# =======Draft-Code========

#  print("===SNAKE--WATER--GUN===")
# print("The computer have chosen it's answer")#

# import random as rd                                                 #using the random module to let the system pick randomly from snake water or gun

# s = "snake"
# w = "water"
# g = "gun"

# options = [s,w,g]
# computer = rd.choice(options)                                       #picks out randomly s.w.g and store it in computer


# player = input("Enter your options[snake,water or gun]: ").lower()  #takes the user input and stores it in the variable player


# if player == "snake" and computer == "water":                       #incase the player chooses snake this code of blocks run it
#     print(f"You win, the computer option was {computer}")
# elif player == "snake" and computer == "gun":
#     print(f"You lose, computer option was {computer}")
# elif player == computer:
#     print(f"The match is a draw, computer option was also {computer}")

# if player == "water" and computer == "gun":                         #incase the player chooses water this code of blocks run it
#     print(f"You win, the computer option was {computer}")
# elif player == "water" and computer == "snake":
#     print(f"You lose, computer option was {computer}")
# elif player == computer:
#     print(f"The match is a draw, computer option was also {computer}")

# if player == "gun" and computer == "snake":                         #incase the player chooses gun this code of blocks run it
#     print(f"You win, the computer option was {computer}")
# elif player == "gun" and computer == "water":
#     print(f"You lose, computer option was {computer}")
# elif player == computer:
#     print(f"The match is a draw, computer option was also {computer}")

# efficient code more structured

print("===SNAKE--WATER--GUN===")
print("The computer have chosen it's answer")#

import random as rd                                                 #using the random module to let the system pick randomly from snake water or gun

s = "snake"
w = "water"
g = "gun"

options = [s,w,g]
computer = rd.choice(options)                                       #picks out randomly s.w.g and store it in computer


player = input("Enter your options[snake,water or gun]: ").lower()

if player == computer:
    print(f"The match ended in a draw. The computer choose{computer}")
elif(player=="snake" and computer=="water") or (player=="water" and computer=="gun") or(player=="gun"and computer=="gun"):
    print(f"You win. The computer choose {computer}")
else:
    print(f"You lose. The computer choose {computer}")
    

