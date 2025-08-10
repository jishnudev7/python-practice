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
computer=[rock,paper,scissors]
player_choice=int(input ("enter the choice 0 :rock, choice 1:paper,choice 2:scissor\n "))
if player_choice>0 and player_choice<3:
    print(computer[player_choice])

computer_choice=random.randint(0,2)
print(computer[computer_choice])

if computer_choice==0 and player_choice==1:
    print("you win")
elif computer_choice==1 and player_choice==2:
    print("you win")
elif computer_choice==2 and player_choice==0:
    print("you win")
elif computer_choice==0 and player_choice==2:
    print("you lose")
elif computer_choice==1 and player_choice==0:
    print("you lose")
elif computer_choice==2 and player_choice==1:
    print("you win")
if (computer_choice==0 and player_choice==0) or (computer_choice==1 and player_choice==1) or (computer_choice==2 and player_choice==2):
    print("tie match try again")