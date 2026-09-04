import random 

high_Score = None

while True:
    print("\n Number Guessing Game")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = int(input("Enter the dificulty level: "))

    if choice == 1:
        max_number = 50
        max_attempts = 10
    elif choice == 2:
        max_number = 75
        max_attempts = 7
    elif choice == 3:
        max_number = 100
        max_attempts = 4
    else:
        print("Invalid choice! Continue Again")
        continue

    secret = random.randint(1, max_number)  #Generate a secret number

    print(f"You have numbers between 1 and {max_number}.\n")
    print(f"You have got {max_attempts} chances.")

    for attempt in range(1, max_attempts+1):
        try:
            guess = int(input(f"\n Attempt {attempt} : Enter your guess: "))    #Guess the number
        except ValueError:
            print("Enter a valid number")
            continue

        if guess < secret:
            print("Number is low. Guess higher")
        elif guess > secret:
            print("Number is high. Guess lower")
        else:
            print(f"Correct! The number was {secret}.")
            print(f"You guessed it in {attempt} attempts.")

            if high_Score is None or attempt < high_Score:  # New High Score
                high_Score = attempt
                print("New High Score🎉🎉")

            print(f"High Score: {high_Score} attempts.")

    else:
        print("\n Attemtps are exhausted.")
        print(f"Game Over😞😞")
        print(f"The correct answer was {secret}.")

    play_again = input("\n Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank You for playing..")
        break
