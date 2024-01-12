import random

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
game_images = [rock, paper, scissors]

choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print(game_images[choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[computer_choice])

# print("What do you choose ? Type 0 for rock , 1 for Paper or 2 for scissors")
# rock = 0
# paper = 1
# scissors = 2
# computer_choice = random.randint(0,2)
# choice = int(input())
# if choice == 0:
#     print(rock)
# elif choice == 1:
#     print(paper)
# elif choice == 2:
#     print(scissors)
# else:
#     print("Please  input the right number")
if choice == 0 and computer_choice == 0:
  print("It's a tie")
elif choice == 0 and computer_choice == 1:
  print("You lose")
elif choice == 0 and computer_choice == 2:
  print("You win")
elif choice == 1 and computer_choice == 1:
  print("tie")
elif choice == 1 and computer_choice == 2:
  print("You lose")
elif choice == 1 and computer_choice == 0:
  print("You win")
elif choice == 2 and computer_choice == 2:
  print("tie")
elif choice == 2 and computer_choice == 0:
  print("You lose")
elif choice == 2 and computer_choice == 1:
  print("You win")
elif choice > 2:
  print("Please enter the right number")
