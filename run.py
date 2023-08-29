# Your code goes here.
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from brands import brands


def get_valid_brand(brands):
    brand = random.choice(brands)
    while ' ' in brand:
        brand = random.choice(brands)
    return brand.upper()

def motorman(brand):
    brand_completion = "_" * len(brand)
    guessed = False
    used_letter = []
    guessed_letter = []
    guessed_word = []
    guessed = False
    lives = 6


    print("Let's play motorman!")
    print(brand_completion)
    print(display_hangman(lives))
    print("\n")



    while not guessed and lives > 0:
        guess = input("please guess a letter:").upper()
        if len(guess) == 1 and guess.isalpha():
           if guess not in brand:
              print(guess,"is not a letter in the brand word")
              lives -= 1
              guessed_letter.append(guess)
           elif guess in guessed_letter:
              print("you already guessed the letter" , guess)
           else:
              print("nice work", guess, "is in the brand word")
              guessed_letter.append(guess)
              brand_as_list = list(brand_completion)
              indices = [i for i, letter in enumerate(brand) if letter == guess]
              for index in indices:
                  brand_as_list[index] = guess
              brand_completion = "".join(brand_as_list)
              if "_" not in brand_completion:
                    guessed = True


        elif len(guess) == len(brand) and guess.isalpha():
            if guess in guessed_word:
                print("You already guessed the word", guess)
            elif guess != brand:
                print(guess, "is not the brand word.")
                lives -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                brand_completion = brand

        else:
            print ("invalid character")
        print(display_hangman(lives))
        print(brand_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + brand + ". Maybe next time!")



def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]







def main():
    brand = get_valid_brand(brands)
    motorman(brand)
    while input("Play Again? (Y/N) ").upper() == "Y":
        brand = get_valid_brand(brands)
        motorman(brand)


if __name__ == "__main__":
    main()