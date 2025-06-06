import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Return a random word from the word list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display current stage of snowman and guessed letters of the word."""
    print(STAGES[mistakes])
    display = " ".join([
        letter if letter in guessed_letters else "_" for letter in secret_word
    ])
    print(f"\nWord: {display}")
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}\n")


def play_game():
    """Main loop for a single round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input(
            "Guess a letter or try the whole word.\n"
            "Be aware: if you guess the wrong word,\n"
            "the snowman melts instantly!\n"
            "Your guess: "
        ).lower().strip()

        # Input must be alphabetic
        if not guess.isalpha():
            print("Please enter only letters.")
            continue

        # Handle full word guess
        if len(guess) > 1:
            if guess == secret_word:
                print(f"Correct! The word was '{secret_word}'. You saved the snowman! 🧤")
                display_game_state(mistakes, secret_word, guessed_letters)
                return
            else:
                print("Wrong word! The snowman melted completely. ☠️")
                mistakes = max_mistakes
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"Game Over! The word was '{secret_word}'.")
                return

        # Handle single letter guess
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Wrong guess!")
            mistakes += 1

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Game Over! The word was '{secret_word}'.")
            return

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Congratulations! You guessed the word '{secret_word}' and saved the snowman! 🎉")
            return