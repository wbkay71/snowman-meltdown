import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Returns a random word from the WORDS list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current guessed state of the word."""
    print(STAGES[mistakes])
    display = [
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ]
    print("Word: " + " ".join(display))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n")


def play_game():
    """Main game loop for playing Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print("Can you save the snowman before he melts?\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!\n")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"🎉 You saved the snowman! The word was '{secret_word}'.")
            break

        # Check lose condition
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"💀 The snowman melted! The word was '{secret_word}'.")
            break