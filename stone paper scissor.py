import random

def get_user_choice():
    while True:
        user_choice = input("Choose s (for stone), p (for paper), or sc (for scissors): ").lower()
        if user_choice in ["s", "p", "sc"]:
            return user_choice
        else:
            print("Invalid choice. Please choose s, p, or sc.")

def get_computer_choice():
    return random.choice(["s", "p", "sc"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "s" and computer_choice == "sc") or
        (user_choice == "sc" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "s")
    ):
        return "You win!"
    return "Computer wins!"

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    if result == "You win!":
        user_score += 1
        print("Congratulations, you win the game!")
    elif result == "Computer wins!":
        computer_score += 1
        print("Sorry, you lost. Better luck next time.")

    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
