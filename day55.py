#game
import random

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'snake' and computer_choice == 'water') or \
         (player_choice == 'water' and computer_choice == 'gun') or \
         (player_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "You lose!"

def main():
    choices = ['snake', 'water', 'gun']
    
    print("Welcome to Snake Water Gun Game!")
    print("Enter your choice (snake, water, gun) or 'quit' to exit.")
    
    while True:
        player_choice = input("Your choice: ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer choice: {computer_choice}")

        result = check_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
