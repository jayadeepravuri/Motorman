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
    while ' ' in brand:
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
    print(" \\_____\\___/|_| |_|\\__, |_|  \\__,_|\\__|___/")
    print("                  __/ |                    ")
    print("                  |___/                    ")


def display_loser_message(brand):
    """Displays the loser message."""
    print(f"Sorry, you ran out of lives. The car brand was {brand}.")


def motorman(brand):
    """Runs the main game logic for Motorman."""
    brand_completion = "-" * len(brand)
    guessed = False
    guessed_letters = set()
    guessed_words = set()
    lives = 5

    print("Let's play Motorman!\n")
    print(brand_completion)
    print(build_motorman(lives))
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter or the word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in brand:
                print(f"{guess} is not in the brand word.")
                lives -= 1
                guessed_letters.add(guess)
            else:
                print(f"Nice work! {guess} is in the brand word.")
                guessed_letters.add(guess)
                brand_completion = ''.join(
                    [guess if brand[i] == guess else char for i, char in enumerate(brand_completion)]
                )
                if '-' not in brand_completion:
                    guessed = True
        elif len(guess) == len(brand) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != brand:
                print(f"{guess} is not the brand word.")
                lives -= 1
                guessed_words.add(guess)
            else:
                guessed = True
                brand_completion = brand
        else:
            print("Invalid input.")

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
