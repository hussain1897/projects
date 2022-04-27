import random

user_wins = 0 
cpu_wins = 0
print("Welcome to Rock/Paper/Scissors !")

options = ["r", "p", "s"]
print("R for rock, P for paper, S for scissors and Q for quit.")

while True:
    user_input = input("Type R/P/S or Q: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    cpu_pick = options[random_number]
    print("CPU Picked:", cpu_pick)

    if user_input == "r" and cpu_pick == "s":
        print(" You Won!")
        user_wins += 1
        
    elif user_input == "p" and cpu_pick == "r":
        print(" You Won!")
        user_wins += 1
        
    elif user_input == "s" and cpu_pick == "p":
        print(" You Won!")
        user_wins += 1
    else:
        print("You Lost")
        cpu_wins += 1

print("You won", user_wins, "times.")
print("The CPU won", cpu_wins, "times.")

print("Thanks for playing")