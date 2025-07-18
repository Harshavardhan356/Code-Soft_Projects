import random

print("=== Welcome to Rock-Paper-Scissors Game ===\n")

print("Instructions:")
print("You will play against the computer.")
print("Choices are: rock, paper, or scissors.\n")


user_score = 0
computer_score = 0
rounds_played = 0


while True:
    print("\nRound", rounds_played + 1)

    
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        continue

    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    rounds_played += 1

    print("Result:", result)
    print(f"Score: You = {user_score} | Computer = {computer_score}")

    
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nThanks for playing the game!")
        print(f"Total Rounds Played: {rounds_played}")
        print(f"Final Score - You: {user_score} | Computer: {computer_score}")

        # decide final winner
        if user_score > computer_score:
            print("Congratulations! You won the game overall")
        elif computer_score > user_score:
            print("Computer wins overall. Better luck next time!")
        else:
            print("It's an overall tie.")
        break
