
import random

# Slot machine symbols
symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]

def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

def check_win(reels):
    if reels[0] == reels[1] == reels[2]:
        return "🎉 Jackpot! You won!"
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return "😊 You got a small win!"
    else:
        return "😞 Try again!"

def play_slot_machine():
    print("🎰 Welcome to the Slot Machine!")
    while True:
        input("Press Enter to spin... ")
        reels = spin_reels()
        print(" | ".join(reels))
        print(check_win(reels))

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_slot_machine()
