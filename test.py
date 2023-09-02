# Your code goes here.
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from brands import brands
import string
import os


def username():
    username = ""
    while True:

        username = input("Welcome! Please Entre a Username: \n")
        if username.isalpha() is True:
           print("------------------------------------------")
           print(f"Hello {username}, Let's play Motorman!\n")
           print(" __  __       _                                   ")
           print("|  \/  |     | |                                  ")
           print("| \  / | ___ | |_ ___  _ __ _ __ ___   __ _ _ __  ")
           print("| |\/| |/ _ \| __/ _ \| '__| '_ ` _ \ / _` | '_ \ ")
           print("| |  | | (_) | || (_) | |  | | | | | | (_| | | | |")
           print("|_|  |_|\___/ \__\___/|_|  |_| |_| |_|\__,_|_| |_|\n")
           print("The rules are simple, guess a car brand , by entering a letter or a word\n")
           print("You have to guess it within 6 attempts to Win!\n")
           return username
        else:
            print("Invalid character. Please enter in alphabets.")
            print("-----------------------------------------------")
            continue


def clear():
    """
    Function to clear the terminal, called when terminal gets crowded.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_brand(brands):
    brand = random.choice(brands)
    while ' ' in brand:
        brand = random.choice(brands)
    return brand.upper()


def motorman(brand):
    brand_completion = "-" * len(brand)
    guessed = False
    alphabet = set(string.ascii_uppercase)
    guessed_letter = []
    guessed_word = []
    guessed = False
    lives = 5
    print("Let's play motorman!")
    print("\n")
    print(brand_completion)
    print(build_motorman(lives))
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You already guessed the letter", guess)
            elif guess not in brand:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letter.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letter.append(guess)
                brand_as_list = list(brand_completion)
                indices = [i for i, letter in enumerate(brand) if letter == guess]
                for index in indices:
                    brand_as_list[index] = guess
                brand_completion = "".join(brand_as_list)
                if "-" not in brand_completion:
                    guessed = True
        elif len(guess) == len(brand) and guess.isalpha():
            if guess in guessed_word:
                print("You already guessed the word", guess)
            elif guess != brand:
                print(guess, "is not the word.")
                lives -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                brand_completion = brand
        else:
            print("Not a valid guess.")
        print(build_motorman(lives))
        print(brand_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + brand + ". Maybe next time!")


def build_motorman(lives):
    stages = [  
                """
               
                \___/          \___/
                """,
                """

                |_| (O) |________| (O) |____|
                   \___/          \___/
                """,
                """

                |  /   \   |___/  /   \  `-.
                |_| (O) |________| (O) |____|
                   \___/          \___/
                """,
                """
                
                |   ___    |  ,|   ___`-.
                |  /   \   |___/  /   \  `-.
                |_| (O) |________| (O) |____|
                   \___/          \___/
                """,
                """
                                  
                __/__\___________| \_
                |   ___    |  ,|   ___`-.
                |  /   \   |___/  /   \  `-.
                |_| (O) |________| (O) |____|
                   \___/          \___/
                """,
                """

                   __            ||
                __/__\___________| \_
                |   ___    |  ,|   ___`-.
                |  /   \   |___/  /   \  `-.
                |_| (O) |________| (O) |____|
                   \___/          \___/
                """         
    ]

    return stages[lives]


def main():
    clear()
    username()
    brand = get_valid_brand(brands)
    motorman(brand)
    while True:
        question = input("Would you like to play again? (Y/N) ").upper()
        if question.upper() == "N":
            clear()
            print("Thank you for playing")
            print("\n")
            print(" __  __       _                                   ")
            print("|  \/  |     | |                                  ")
            print("| \  / | ___ | |_ ___  _ __ _ __ ___   __ _ _ __  ")
            print("| |\/| |/ _ \| __/ _ \| '__| '_ ` _ \ / _` | '_ \ ")
            print("| |  | | (_) | || (_) | |  | | | | | | (_| | | | |")
            print("|_|  |_|\___/ \__\___/|_|  |_| |_| |_|\__,_|_| |_|\n")
            break
            clear()
        elif question.upper() != "Y":
             clear()
             print(f"{question} is not valid. Entre a valid character")
             print("\n")
             question.upper()
        else:
            clear()
            username()
            brand = get_valid_brand(brands)
            motorman(brand)


if __name__ == "__main__":
    main()
    