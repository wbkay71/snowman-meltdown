from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing Snowman Meltdown! Goodbye! ❄️")
            break