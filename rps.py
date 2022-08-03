import random


def game(action_user):
    given_actions = ["rock", "paper", "scissors"]
    action_computer = random.choice(given_actions)
    print("action_computer is", action_computer)
    if action_user == action_computer:
        print("it is a tie")
    elif action_user == "rock":
        if action_computer == "scissors":
            print("rock beat scissors")
        else:
            print("paper beat rock")
    elif action_user == "paper":
        if action_computer == "scissors":
            print("scissors beat paper")
        else:
            print("rock beat scissors")
    elif action_user == "scissors":
        if action_computer == "rock":
            print("rock beat scissors")
        else:
            print("scissors beat paper")


action_user = input("enter your choice:rock,paper,scissors")
game(action_user)

y = input("restart:yes/no")
while y == "yes":
    x = input("enter your choice:rock,paper,scissors")
    game(x)
    y = input("restart:yes/no")