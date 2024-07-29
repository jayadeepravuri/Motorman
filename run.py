import random
import string
import os
from brands import brands


def username():
    """Function to get a valid username."""
    while True:
        user_name = input("Welcome! Please Enter a Name: \n")
        if user_name.isalpha():
            print("------------------------------------------")
            print(f"Hello {user_name}, Let's play Motorman!\n")
            print(" __  __       _                                   ")
            print("|  \\/  |     | |                                  ")
            print("| \\  / | ___ | |_ ___  _ __ _ __ ___   __ _ _ __  ")
            print("| |\\/| |/ _ \\| __/ _ \\| '__| '_ ` _ \\ / _` | '_ \\ ")
            print("| |  | | (_) | || (_) | |  | | | | | | (_| | | | |")
            print("|_|  |_|\\___/ \\__\\___/|_|  |_| |_| |_|\\__,_|_| |_|\n")
            print("The rules are simple, guess a car brand, by entering a letter or a word\n")
            print("You have to guess it within 6 attempts to Win!\n")
            return user_name
        else:
            print("Invalid character. Please enter in alphabets.")
            print("-----------------------------------------------")
            continue


def clear():
    """Function to clear the terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_brand(brands):
    """Function to get a valid brand name without spaces."""
    brand = random.choice(brands)
    while ' ' in brand:
        brand = random.choice(brands)
    return brand.upper()


def build_motorman(lives):
    """Function to build the motorman display based on remaining lives."""
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
    return stages[lives]


def motorman(brand):
    """Function to run the motorman game logic."""
    brand_completion = "-" * len(brand)
    guessed = False
    alphabet = set(string.ascii_uppercase)
    guessed_letters = []
    guessed_words = []
    lives = 5

    print("Let's play motorman!")
    print("\n")
    print(brand_completion)
    print(build_motorman(lives))
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in brand:
                print(f"{guess} is not a letter in the brand word.")
                lives -= 1
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            else:
                print(f"Nice work! {guess} is in the brand word.")
                guessed_letters.append(guess)
                brand_as_list = list(brand_completion)
                indices = [i for i, letter in enumerate(brand) if letter == guess]
                for index in indices:
                    brand_as_list[index] = guess
                brand_completion = "".join(brand_as_list)
                if "-" not in brand_completion:
                    guessed = True
        elif len(guess) == len(brand) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != brand:
                print(f"{guess} is not the brand word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                brand_completion = brand
        else:
            print("Invalid character.")

        print(build_motorman(lives))
        print(brand_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
        print("  _____                            _       ")
        print(" / ____|                          | |      ")
        print("| |     ___  _ __   __ _ _ __ __ _| |_ ___ ")
        print("| |    / _ \\| '_ \\ / _` | '__/ _` | __/ __|")
        print("| |___| (_) | | | | (_| | | | (_| | |_\\__ \\")
        print(" \\_____\\___/|_| |_|\\__, |_|  \\__,_|\\__|___/")
        print("                  __/ |                    ")
        print("                  |___/                    ")
    else:
        print(f"Sorry, you ran out of lives. The car brand was {brand}.")


def main():
    clear()
    username()
    brand = get_valid_brand(brands)
    motorman(brand)
    while True:
        question = input("Would you like to play again? (Y/N) ").upper()
        if question == "N":
            clear()
            print("Thank you for playing")
            print("\n")
            print(" __  __       _                                   ")
            print("|  \\/  |     | |                                  ")
            print("| \\  / | ___ | |_ ___  _ __ _ __ ___   __ _ _ __  ")
            print("| |\\/| |/ _ \\| __/ _ \\| '__| '_ ` _ \\ / _` | '_ \\ ")
            print("| |  | | (_) | || (_) | |  | | | | | | (_| | | | |")
            print("|_|  |_|\\___/ \\__\\___/|_|  |_| |_| |_|\\__,_|_| |_|\n")
            break
        elif question != "Y":
            clear()
            print(f"{question} is not valid. Enter a valid character")
            print("\n")
        else:
            clear()
            username()
            brand = get_valid_brand(brands)
            motorman(brand)


if __name__ == "__main__":
    main()