# Motorman

![Title graphic](/assets/images/title.JPG)
[Here is the live version of my project](https://motorman-002301103e6a.herokuapp.com/)

The popular game of Hangman, has been redesigned and given the name MotorMan. It is a command line interface game and the player should guess a letter or a word within 6 tries, in order to win the game. The game  provides full user interaction to complete the game.

I trust you'll find the game enjoyable.

## Lucid Chart

![Flow Chart](/assets/images/lucid%20chart%201.png)
![Flow Chart](/assets/images/Lucid%20chart%202.png)
Before commencing the game's initial development, I created a flowchart using Lucid Chart to map out my approach to writing the Python code for the game. At the start of the game, my intention was to inquire about the user's name and store it for later use. Additionally, I aimed to confirm the user's category choice and, in case of uncertainty, implement a loop to revisit the question.

The flowchart outlines the Motorman game process:

1. **Start**: Clear terminal.
2. **Username Input**: Prompt user for a valid name.
3. **Game Setup**: Display game rules and select a random brand.
4. **Game Loop**: Players guess letters or the full brand name while tracking lives.
5. **Game Outcome**: Check if the player won (guessed the word) or lost (ran out of lives).
6. **End or Replay**: Prompt the player to replay or end the game.

This ensures a smooth gameplay experience from start to finish.

## Design

![Start of game](/assets/images/Motorman.JPG)

The design element does not feature too much in this project, as it is a command line interface project. Whilst not requiring any ‘glamorous’ design, the function of the app works well enough. I have previously seen some other apps developed by students that hold a little more style, but for the purposes of the game, everything is fine.

### Features

The Motorman game offers a fun and straightforward experience with the following features:

1. **User-Friendly Start**: The game begins by asking for your name, only accepting alphabetic characters, making it simple and easy to get started.

2. **Clean Display**: The screen clears when needed, keeping things organized and clutter-free as you play.

3. **Random Brand Guessing**: A car brand is chosen at random for you to guess, ensuring a fresh challenge each time. The brand names don’t include spaces, so it’s all about finding the right letters.

4. **Interactive Gameplay**: You can guess one letter at a time or go for the entire word. After each guess, your progress is updated, showing which letters you’ve got right so far.

5. **Limited Lives**: You start with 5 lives, and each wrong guess costs you one. It adds a bit of pressure and excitement, as you need to figure out the word before running out of attempts.

6. **Motorman Character**: As you lose lives, a simple character called "Motorman" changes, visually showing your remaining chances. It’s a nice touch that adds some personality to the game.

7. **Win or Lose**: If you guess the brand before running out of lives, you win! If not, the game lets you know what the brand was and displays a message about losing.

8. **Play Again Option**: After the game ends, you can decide whether to try your luck again or call it a day. It’s up to you!

These features make Motorman a fun and easy game to play, with just enough challenge to keep you coming back for more.

### ASCII Art

![ASCII Art](/assets/images/ASCII.JPG)

I was particularly captivated by the idea of integrating ASCII art, a creative graphical technique that employs printable characters to construct visual representations. Given that this game operates within a command-line environment, there was a concern that it might come across as simplistic and unengaging to users. From my viewpoint, there was an opportunity to leverage ASCII art more extensively, potentially to communicate the remaining number of lives.

## Testing

### Validation

I employed CI Python Linter for validation purposes and to ensure the integrity of the code by Code Institute. This tool facilitated comprehensive testing of the entire codebase, including an assessment against PEP8 standards, which govern the readability and consistency of Python code. While the test recommended an alternative method for exiting the program, it's worth noting that my current code functions without errors. Apart from minor readability concerns, which I'll address below, my code adheres to the PEP8 guidelines.
### Unsolved Errors

Testing involved using print statements to check whether a piece of code or function worked before really adding the true purpose of the code. 

![CI Python Linter](/assets/images/error.png)



## Deployment

The following deployment stages were taken. Through Gitpod, I would have to stage regular commits.

* `git add .` - Adds saved files to Git's staging area
* `git commit -m ""` - Commits the saved files to the local repository
* `git push` - Pushes the commits

As this was a command line program, I had to deploy via Heroku. Heroku is a cloud based application platform. I had to use this software to be able to build a terminal in the form of a website, so that the game could be tested and assessed. The following deployment stages are.

* On the settings section of the application dashboard, select config vars.
* Set the Key to PORT and the value to 8000
* Add buildpacks, python and node.js
* From the Deploy tab, deploy manually at the bottom of the page.

The above steps, created a usable application.

## Future Development

* Firstly, the game could have different levels of difficulty, according to category of 
  words.
* The guessed letter could be displayed.
* Multiple letters can be taken instead of a single letter.
* Score system could be added.
* Also the code for me seems very clunky and would definitely benefit from being condensed 
  so that the readability improves significantly.

## Credits and Mentions

* Code institute for the template.
* Youtube for great tutorials and inspiration.
* My family for the suppport.
