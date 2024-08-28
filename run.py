import random
import string
import os
from brands import brands


def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_username():
    """Prompts the user to enter a valid username."""
    while True:
        user_name = input("Welcome! Please Enter a Name: \n")
        if user_name.isalpha():
            print(f"\nHello {user_name}, Let's play Motorman!\n")
            print(" __  __       _                                   ")
            print("|  \\/  |     | |                                  ")
            print("| \\  / | ___ | |_ ___  _ __ _ __ ___   __ _ _ __  ")
            print("| |\\/| |/ _ \\| __/ _ \\| '__| '_ ` _ \\ / _` | '_ \\ ")
            print("| |  | | (_) | || (_) | |  | | | | | | (_| | | | |")
            print("|_|  |_|\\___/ \\__\\___/|_|  |_| |_| |_|\\__,_|_| |_|\n")
            print("The rules are simple, guess a car brand by entering a letter or a word.")
            print("You have to guess it within 6 attempts to win!\n")
            return user_name
        else:
            print("Invalid character. Please enter alphabets only.\n")


def get_valid_brand(brands):
    """Selects a valid brand name from the list (without spaces)."""
    brand = random.choice(brands)
    return brand.upper()


def build_motorman(lives):
    """Returns the motorman display based on the number of remaining lives."""
    stages = [
        r"""
           \___/          \___/
        """,
        r"""
        |_| (O) |________| (O) |____|
           \___/          \___/
        """,
        r"""
        |  /   \   |___/  /   \  `-.
        |_| (O) |________| (O) |____|
           \___/          \___/
        """,
        r"""
        |   ___    |  ,|   ___`-.
        |  /   \   |___/  /   \  `-.
        |_| (O) |________| (O) |____|
           \___/          \___/
        """,
        r"""
        __/__\___________| \_
        |   ___    |  ,|   ___`-.
        |  /   \   |___/  /   \  `-.
        |_| (O) |________| (O) |____|
           \___/          \___/
        """,
        r"""
        __            ||
        __/__\___________| \_
        |   ___    |  ,|   ___`-.
        |  /   \   |___/  /   \  `-.
        |_| (O) |________| (O) |____|
           \___/          \___/
        """
    ]
    return stages[5 - lives]


def display_winner_message():
    """Displays the winner message."""
    print("Congrats, you guessed the word! You win!")
    print("  _____                            _       ")
    print(" / ____|                          | |      ")
    print("| |     ___  _ __   __ _ _ __ __ _| |_ ___ ")
    print("| |    / _ \\| '_ \\ / _` | '__/ _` | __/ __|")
    print("| |___| (_) | | | | (_| | | | (_| | |_\\__ \\")
    print(" \\_____\\___/|_| |_|\\__,|_|  \\__,_|\\__|___/")
    print("                      __/ |                    ")
    print("                      |___/                    ")


def display_loser_message(brand):
    print(f"Sorry, you ran out of lives. The car brand was {brand}.")


def process_guess(guess, brand, guessed_letters, guessed_words, brand_completion):
    """
    A unified Guess handling approach.
    Processes the player's guess and updates the game state accordingly.
    """
    if len(guess) == 1:  # Guessing a letter
        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}.")
            return brand_completion, 0, False  # No life lost, not guessed
        guessed_letters.add(guess)
        if guess in brand:
            print(f"Good guess! {guess} is in the brand.")
            brand_completion = ''.join(
                [guess if brand[i] == guess else char for i, char in enumerate(brand_completion)]
            )
            return brand_completion, 0, brand_completion == brand  # No life lost, check if guessed
        else:
            print(f"Sorry, {guess} is not in the brand.")
            return brand_completion, 1, False  # Life lost, not guessed
    else:  # Guessing the entire word
        if guess in guessed_words:
            print(f"You've already guessed the word {guess}.")
            return brand_completion, 0, False  # No life lost, not guessed
        guessed_words.add(guess)
        if guess == brand:
            return brand, 0, True  # Correct guess, game won
        else:
            print(f"Sorry, {guess} is not the correct brand.")
            return brand_completion, 1, False  # Life lost, not guessed


def motorman(brand):
  
    brand_completion = "-" * len(brand)
    guessed_letters = set()
    guessed_words = set()
    lives = 5
    guessed = False

    print("Let's play Motorman!\n")
    print(brand_completion)
    print(build_motorman(lives))
    print("\n")

    while lives > 0 and not guessed:
        guess = input("Please guess a letter or the word: ").upper()
        if not guess.isalpha():
            print("Invalid input. Please enter only letters.")
            continue  

        # Process the guess and update the game state
        brand_completion, lives_lost, guessed = process_guess(
            guess, brand, guessed_letters, guessed_words, brand_completion
        )
        lives -= lives_lost  

        print(build_motorman(lives))
        print(brand_completion)
        print("\n")

    if guessed:
        display_winner_message()
    else:
        display_loser_message(brand)


def main():
    while True:
        clear_terminal()
        get_username()
        brand = get_valid_brand(brands)
        motorman(brand)
        while True:
            play_again = input("Would you like to play again? (Y/N) ").upper()
            if play_again == 'N':
                clear_terminal()
                print("Thank you for playing Motorman!")
                return
            elif play_again == 'Y':
                break
            else:
                print(f"{play_again} is not valid. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    main()
