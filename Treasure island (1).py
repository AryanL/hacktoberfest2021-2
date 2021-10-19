print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are at a cross road. Where do you want to go? Type 'left' or 'right' ")
a=input()
if a.lower() == "left" :
  print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat ot Type'swim' to swim across river")
  b=input()
  if "wait" == b.lower():
    print("You have arrived at the island unharmed. There is ahouse with 3 doors. Red,blue and yellow. Which colour do you choose?")
    c=input()
    if "yellow" == c.lower():
      print("Congratulations, You have found the treasure!!!!!")
    elif "red" == c.lower():
      print("Burned by fire. GAME OVER!")
    elif "blue" == c.lower():
      print("Eaten by beasts. GAME OVER!")
    else:
      print("GAME OVER!")
  else:
    print("Attacked by trout. GAME OVER!")
else:
  print("You fell into a hole. GAME OVER!")



