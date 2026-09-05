import random

choices = ["rock", "paper", "scissors"]
computer_wins = 0
user_wins = 0
tie = 0

while True:
    user_choice = input("Enter your choice(rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Enter again!!!")

    else:
        comp_choice = random.choice(choices)    #Random choice for customer

        print(f"Computer's choice is: {comp_choice}")
        print(f"Your choice is: {user_choice}")

        if user_choice == comp_choice:
            print("It is a tie!!!")
            tie += 1
        elif user_choice == "rock" and comp_choice == "scissors" or \
            user_choice == "paper" and comp_choice == "rock" or \
            user_choice == "scissors" and comp_choice == "paper":
            print("Congratulation! You won!!!")
            user_wins += 1
        else:
            print("Computer win")
            computer_wins += 1

    play_again = input("Enter 'y' to play again or any other key to exit: ").lower()

    if play_again != 'y':
        print("Thank You for playing!!!")
        break

print("=======Final Score=======")
print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Ties: {tie}")