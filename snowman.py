import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Shows the current stage of the snowman and the word
    with unguessed letters replaced by underscores.
    """
    # Show the ASCII snowman stage based on how many mistakes were made
    print(STAGES[mistakes])

    # Build the word display: show each letter or underscore
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word so far:", display.strip())
    print("Guessed letters:", " ".join(guessed_letters))


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected!")  # später ausblenden oder nur für Debug

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        # Noch keine Logik – das kommt später!
        # Wir fügen einfach jeden Buchstaben zur Liste hinzu
        guessed_letters.append(guess)

        # Zum Testen erhöhen wir die Fehlerzahl bei jedem Durchlauf
        mistakes += 1

    print("\nGame Over!")
    display_game_state(mistakes, secret_word, guessed_letters)


if __name__ == "__main__":
    play_game()