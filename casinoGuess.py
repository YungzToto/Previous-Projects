import random
import time

def randnum():
    return random.randint(1, 10)

def main():
    print("\n\nCASINO GUESSING GAME\n\n")
    
    try:
        amount = int(input("Please enter your deposit to play the game: $"))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    while True:
        if amount == 0:
            print("Sorry. All your money is gone!\n")
            break
        
        try:
            bet = int(input(f"\nYour current balance is ${amount}\nPlease enter the amount of money you want to bet with: $"))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        if bet > amount:
            print("\nSorry. You don't have enough money to play!\n")
            continue
        
        if bet <= 0:
            print("\nBet must be greater than 0!\n")
            continue
        
        try:
            a = int(input("Please guess a number between 1 and 10: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        if a > 10 or a <= 0:
            print("\nYou picked the wrong number. Please try again!")
            continue
        
        # Random number generator
        random.seed(time.time())
        x = randnum()
        
        if a == x:
            amount = amount + (bet * 10)
            print(f"\nCongratulations! You guessed correctly! You've won: ${bet * 10}")
        else:
            amount = amount - bet
            print(f"\nSorry. The correct number was {x}. You've just lost: ${bet}")
        
        print(f"Thanks for playing. Your balance amount is: ${amount}")
        
        # Ask if player wants to continue
        if amount > 0:
            choice = input("\nDo you want to play again? (y/n): ").lower()
            if choice != 'y':
                print(f"\nGame over! You're leaving with: ${amount}")
                break
        else:
            print("\nGame over! You're out of money!")
            break

if __name__ == "__main__":
    main()
