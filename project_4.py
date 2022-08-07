import random
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
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

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

hand = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors "))
print(hand[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(hand[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!!!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
if computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("DRAW")