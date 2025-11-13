print("Welcome to Rock-Paper-Scissors!")

# Computer Output
import random
choices = ["Scissors", "Rock", "Paper"]
comp_choice = random.choice(choices)

print(f"Computer chose: {comp_choice}")
# Player's Input
choice = input("choose rock, paper, or scissors: ")

print(f"You chose: {choice.lower().strip()}")
