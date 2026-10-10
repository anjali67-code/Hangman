import random

# ---------------------------------------------------------------
# Words and hints
# ---------------------------------------------------------------
WORDS = [
    {"word": "rose",     "hint": "A red flower with thorns"},
    {"word": "piano",    "hint": "Has 88 keys but no locks"},
    {"word": "guitar",   "hint": "Has six strings and a wooden body"},
    {"word": "penguin",  "hint": "A bird in a tuxedo that can't fly"},
    {"word": "castle",   "hint": "A king's home with towers and a moat"},
    {"word": "diamond",  "hint": "The hardest gemstone, sparkles brightly"},
    {"word": "volcano",  "hint": "A mountain that erupts with lava"},
    {"word": "umbrella", "hint": "You hold it when it rains"},
]

# ---------------------------------------------------------------
# ASCII art for each stage (0 = no wrong guesses, 6 = game over)
# ---------------------------------------------------------------
HANGMAN_PICS = [
    [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "=========",
    ],
    [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "=========",
    ],
]


# ---------------------------------------------------------------
# Display helper
# ---------------------------------------------------------------
def display_state(word, guessed_letters, wrong_guesses):
    """Show the hangman, current word progress, and guessed letters."""
    # Print the hangman picture line by line
    for line in HANGMAN_PICS[len(wrong_guesses)]:
        print(line)

    # Show the word with underscores for unguessed letters
    display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display}")

    wrong = ', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'
    print(f"\nWrong guesses ({len(wrong_guesses)}/6): {wrong}")
    print("-" * 40)


# ---------------------------------------------------------------
# Main game logic
# ---------------------------------------------------------------
def play_hangman():
    entry = random.choice(WORDS)
    word = entry["word"]
    hint = entry["hint"]

    guessed_letters = set()
    wrong_guesses = set()
    max_wrong = 6

    print("=" * 40)
    print("       Welcome to Hangman!")
    print("=" * 40)
    print(f"\nHint: {hint}\n")

    while len(wrong_guesses) < max_wrong:
        display_state(word, guessed_letters, wrong_guesses)

        # Win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was: {word}")
            return

        # Player input
        guess = input("\nGuess a letter (or type 'hint'): ").lower().strip()

        if guess == "hint":
            print(f"Hint: {hint}")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"You already guessed '{guess}'. Try another.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")

    # Game over
    display_state(word, guessed_letters, wrong_guesses)
    print(f"\nGame over! The word was: {word}")


# ---------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------
def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print("\n" * 2)


if __name__ == "__main__":
    main()